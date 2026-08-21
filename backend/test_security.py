from app.utils.security import validate_sql


def test_query(sql: str):
    print("\n" + "=" * 70)
    print("INPUT:")
    print(sql)

    result = validate_sql(sql)

    print("\nVALID:", result.is_valid)

    if result.error_message:
        print("ERROR:", result.error_message)

    if result.sql:
        print("SQL TO EXECUTE:")
        print(result.sql)


# 1. Safe SELECT
test_query(
    "SELECT * FROM customers"
)

# 2. Safe SELECT with LIMIT
test_query(
    "SELECT * FROM customers LIMIT 10"
)

# 3. UPDATE should fail
test_query(
    "UPDATE customers SET first_name = 'HACKED'"
)

# 4. DELETE should fail
test_query(
    "DELETE FROM customers"
)

# 5. DROP should fail
test_query(
    "DROP TABLE customers"
)

# 6. Multiple statements should fail
test_query(
    "SELECT * FROM customers; DROP TABLE orders"
)

# 7. Unauthorized table should fail
test_query(
    "SELECT * FROM pg_catalog.pg_tables"
)

# 8. Another unauthorized table
test_query(
    "SELECT * FROM information_schema.tables"
)

# 9. Safe JOIN
test_query(
    """
    SELECT
        customers.first_name,
        customers.last_name,
        orders.order_date
    FROM customers
    JOIN orders
        ON customers.id = orders.customer_id
    """
)

# 10. Comment injection
test_query(
    "SELECT * FROM customers -- DROP TABLE customers"
)