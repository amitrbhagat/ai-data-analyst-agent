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



def generate_sql(question:str) -> SQLGenerationResult:


    # build sql prompt
    prompt = build_sql_prompt(question);

    # send prompt to the provider
    response = provide_response(prompt, temperature=0.1)

    # convert the response into dictionary
    try:
        parsed_response = json.loads(response)

    except json.JSONDecodeError as e:
        print("LLM returned invalid JSON.")
        print(f"Raw response: {response}")
        raise ValueError("LLM returned invalid JSON.") from e


    # 4. Validate response using Pydantic
    try:
        result = SQLGenerationResult(**parsed_response)

    except ValidationError as e:
        print("LLM response failed Pydantic validation.")
        print(e)
        raise ValueError("Invalid SQL generation response.") from e


    return result



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

