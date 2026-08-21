# Define the prompt which needs to be send to the LLm with instructions, Use question, 
# Schema description (sql.py) and format in which answer should be return (schema.py)


from app.database.schema import get_schema_description
from app.schemas.sql import SQLGenerationResult



def build_sql_prompt(user_question: str) -> str:

    schema = get_schema_description()

    return f"""
    
You are a PostgreSQL SQL expert.

You are working with the following database:


DATABASE SCHEMA:
{schema}

RULES:
1. Only generate SELECT or WITH statements.
2. Never generate INSERT, UPDATE, DELETE, DROP, ALTER, TRUNCATE,
   CREATE, GRANT, or REVOKE statements.
3. This is a read-only analytics system.
4. Only use tables and columns that exist in the provided schema.
5. Never invent table names or column names.
6. Use valid PostgreSQL syntax.
7. When calculating revenue, use quantity * unit_price.
8. When calculating revenue, include only orders with status = 'completed'.
9. Generate the simplest correct SQL query that answers the user's question.
10. Do not include markdown code fences.
11. Do not include any text outside the JSON response.

USER QUESTION:
{user_question}


OUTPUT FORMAT:
Return ONLY valid JSON using exactly this structure:

{{
    "sql": "your PostgreSQL query here",
    "reasoning_summary": "One short sentence explaining the SQL approach.",
    "confidence": 0.0
}}

The confidence value must be a number between 0.0 and 1.0.

Do not return anything before or after the JSON.
"""



# if __name__ == "__main__":
#     user_question = "What is total_revenue from month July"
#     res = build_sql_prompt(user_question)
#     print(res)
