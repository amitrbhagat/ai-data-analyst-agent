# Here we will connect  
# schema.py
#    → describes the database

# sql.py
#     → defines the expected JSON structure

# sql_generation.py
#     → builds the prompt

# provider.py
#     → talks to TinyLlama

import pandas as pd
from app.database.connection import get_readonly_engine
from app.utils.security import validate_sql
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from pydantic import ValidationError
from app.agents.prompts.sql_generation import build_sql_prompt
from app.llm.provider import provide_response
from app.schemas.sql import SQLGenerationResult
import json
from app.agents.prompts.sql_fix import build_sql_fix_prompt




def _call_llm_for_sql(prompt:str) -> SQLGenerationResult:

    response = provide_response(
        prompt,
        temperature=0.1
    )
    
    response = response.strip()

    if response.startswith("```json"):
        response = response[7:]

    elif response.startswith("```"):
        response = response[3:]

    if response.endswith("```"):
        response = response[:-3]

    response = response.strip()

    try:
        parsed_response = json.loads(response)

    except json.JSONDecodeError as e:
        print("LLM return invalid json")
        print(f"Raw Response: {response}")

        raise ValueError(
            "LLM return invalidJSON"
        ) from e        

    try:
        result = SQLGenerationResult(
            **parsed_response
        )

    except ValidationError as e:
        print("LLM response failed Pydantic validation.")
        print(e)

        raise ValueError(
            "Invalid SQL generation response."
        ) from e

    return result



def generate_sql(question:str) -> SQLGenerationResult:

    prompt = build_sql_prompt(question);

    return _call_llm_for_sql(prompt)
    



def execute_sql(sql:str) -> pd.DataFrame:

    validation_result = validate_sql(sql)

    if not validation_result.is_valid:
        raise ValueError(
            f"SQL validation failed: "
            f"{validation_result.error_message}"
        )

    readonly_engine = get_readonly_engine()

    try:
        with readonly_engine.connect() as connection:

            with connection.begin():

                # PostgreSQL timeout for this transaction
                connection.execute(
                    text("SET LOCAL statement_timeout = 5000")
                )

                # Execute query and return Pandas DataFrame
                dataframe = pd.read_sql_query(
                    text(validation_result.sql),
                    connection,
                )

                return dataframe

    except SQLAlchemyError as e:
        raise RuntimeError(
            f"SQL execution failed: {str(e)}"
        ) from e


    except Exception as e:
        raise RuntimeError(
            f"Unexpected SQL execution error: {str(e)}"
        ) from e    


def generate_and_execute_sql(question:str, max_retries: int = 1) ->dict:

    if max_retries < 0:
        raise ValueError(
            "max_retries must be greater than or equal to 0."
        )

    try:
        generation_result = generate_sql(question)

    except Exception as e:

        return {
            "success": False,
            "dataframe": None,
            "final_sql":None,
            "attempts":1,
            "error_message":(
                f"Initial SQL generation failed: {str(e)}"
            )
        }

    current_sql = generation_result.sql

    for retry_number in range(max_retries + 1):

        attempt_number = retry_number + 1

        try:
            dataframe = execute_sql(current_sql)

            return {
                "success": True,
                "dataframe": dataframe,
                "final_sql": current_sql,
                "attempts": attempt_number,
                "error_message": None
            }

        except (ValueError, RuntimeError) as e:

            error_message = str(e)

            print(
                f"SQL attempt {attempt_number} failed :"
            )
            print(error_message)

            if(retry_number >= max_retries):

                return {
                    "success": False,
                    "dataframe": None,
                    "final_sql": current_sql,
                    "attempts": attempt_number,
                    "error_message": (
                        f"Could not generate valid SQL "
                        f"after {attempt_number} attempts. "
                        f"Last error: {error_message}"
                    )
                }

            fixed_prompt = build_sql_fix_prompt(
                question=question,
                previous_sql=current_sql,
                error_message=error_message
            )

            try:

                fixed_result = _call_llm_for_sql(fixed_prompt)

            except Exception as e:

                return {
                    "success": False,
                    "dataframe": None,
                    "final_sql": current_sql,
                    "attempts": attempt_number + 1,
                    "error_message": (
                        f"SQL fix generation failed: "
                        f"{str(e)}"
                    )
                }

            current_sql = fixed_result.sql

    return {
        "success": False,
        "dataframe": None,
        "final_sql": current_sql,
        "attempts": max_retries + 1,
        "error_message": "SQL pipeline stopped unexpectedly."
    }
               