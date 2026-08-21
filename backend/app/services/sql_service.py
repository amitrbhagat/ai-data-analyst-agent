# Here we will connect  
# schema.py
#    → describes the database

# sql.py
#     → defines the expected JSON structure

# sql_generation.py
#     → builds the prompt

# provider.py
#     → talks to TinyLlama


from pydantic import ValidationError

from app.agents.prompts.sql_generation import build_sql_prompt
from app.llm.provider import provide_response
from app.schemas.sql import SQLGenerationResult
from app.database.schema import get_schema_description
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



