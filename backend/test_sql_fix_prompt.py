from app.agents.prompts.sql_fix import build_sql_fix_prompt



question = "What is the total revenue?"

previous_sql = """
SELECT SUM(total_revenu)
FROM orders
"""

error_message = 'column "total_revenu" does not exist'

prompt = build_sql_fix_prompt(
    question=question,
    previous_sql=previous_sql,
    error_message=error_message
)

print("=" * 80)
print("SQL FIX PROMPT")
print("=" * 80)
print(prompt)
