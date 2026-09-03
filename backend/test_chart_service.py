from app.services.chart_service import decide_chart


# Test 1: Monthly revenue
monthly_revenue = [
    {"month": "2025-01", "revenue": 12000},
    {"month": "2025-02", "revenue": 15000},
    {"month": "2025-03", "revenue": 18000},
]

result = decide_chart(monthly_revenue)

print("Monthly Revenue:")
print(result)


# Test 2: Top 5 products
top_products = [
    {"product_name": "Laptop", "revenue": 50000},
    {"product_name": "Phone", "revenue": 42000},
    {"product_name": "Tablet", "revenue": 31000},
    {"product_name": "Monitor", "revenue": 25000},
    {"product_name": "Keyboard", "revenue": 12000},
]

result = decide_chart(top_products)

print("\nTop Products:")
print(result)


# Test 3: Total revenue
total_revenue = [
    {"total_revenue": 175000}
]

result = decide_chart(total_revenue)

print("\nTotal Revenue:")
print(result)
