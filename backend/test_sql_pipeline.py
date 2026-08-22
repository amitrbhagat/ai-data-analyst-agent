from app.services.sql_service import generate_and_execute_sql

question = "What is the total revenue?"

result = generate_and_execute_sql(question, max_retries=1)

print("\n" + "=" * 80)
print("SQL PIPELINE RESULT")
print("=" * 80)

print("Success:", result["success"])
print("Attempts:", result["attempts"])
print("Final SQL:", result["final_sql"])
print("Error:", result["error_message"])

if result["dataframe"] is not None:
    print("\nDataFrame:")
    print(result["dataframe"])
else:
    print("\nNo DataFrame returned.")
