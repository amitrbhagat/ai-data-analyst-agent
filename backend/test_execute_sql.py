from app.services.sql_service import execute_sql

sql = """
SELECT
    COUNT(*) AS customer_count
FROM customers
"""


try:
    result = execute_sql(sql)

    print("SQL executed successfully.")
    print()
    print(result)

except Exception as e:
    print("SQL execution failed:")
    print(e)