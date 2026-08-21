from app.services.sql_service import generate_sql


result = generate_sql("What is the total revenue?")


print("-------sql---------------")
print(result["sql"])

print("-------summary-----------")
print(result["reasoning_summary"])

print("------confidence---------")
print(result["confidence"])
