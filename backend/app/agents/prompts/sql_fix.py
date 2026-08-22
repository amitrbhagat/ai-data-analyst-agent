from app.database.schema import get_schema_description


def build_sql_fix_prompt(question: str, previous_sql: str, error_message: str) -> str:
    schema = get_schema_description()

    return f"""
You are an expert PostgreSQL SQL debugging assistant. 
Your task is to fix a previously generated SQL query that failed validation or database execution.

DATABASE SCHEMA:
{schema}

USER_QUESTION:
{question}

PREVIOUSLY GENERATED SQL:
{previous_sql}

EXACT ERROR MESSAGE:
{error_message}

INSTRUCTIONS: 

1. Analyze why the previous SQL query failed. 
2. Fix the specific problem identified by the error message. 
3. Do not repeat the same mistake. 
4. Make sure the corrected query answers the original user question.
5. Use only tables and columns that exist in the provided database schema. 
6. Use valid PostgreSQL syntax. 
7. The query must be read-only. 
8. Only SELECT or WITH queries are allowed. 
9. Do NOT use INSERT, UPDATE, DELETE, DROP, ALTER, TRUNCATE, CREATE, GRANT, REVOKE, EXECUTE, or any other write/DDL operation. 
10. Do not reference PostgreSQL system tables such as pg_catalog or information_schema. 
11. Do not include SQL comments. 
12. Return only valid JSON. 
13. Do not wrap the JSON in Markdown code fences.

OUTPUT FORMAT:

{{
    "sql": "corrected SQL query",
    "reasoning_summary": "brief explanation of what was wrong and how it was fixed",
    "confidence": 0.0
}}


The confidence value must be a number between 0.0 and 1.0. 
Return ONLY the JSON object.
"""
