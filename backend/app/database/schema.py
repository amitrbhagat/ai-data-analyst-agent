# In schema.py we are creating the one function in which we are giving one prompt to send that to the LLM in which we 
# included Table name, Column name, data typs, description about table data
# Also including the instructions for the LLM model


def get_schema_description() -> str:

    return """
    
Database Schema: 

Table: regions
Purpose: Stores geographic regions.

Columns:
- id: INTEGER, Primary Key
- name: VARCHAR(100), NOT NULL, UNIQUE


Table: customers
Purpose: Stores customers.

Columns:
- id: INTEGER, Primary Key
- first_name: VARCHAR(100), NOT NULL
- last_name: VARCHAR(100), NOT NULL
- email: VARCHAR(100), NOT NULL, UNIQUE
- region_id: INTEGER, Foreign Key -> regions.id
- created_at: TIMESTAMP, NOT NULL


Table: products
Purpose: Stores sellable products.

Columns:
- id: INTEGER, Primary Key
- name: VARCHAR(100), NOT NULL
- category: VARCHAR(100), NOT NULL
- price: NUMERIC(10,2), NOT NULL
- created_at: TIMESTAMP, NOT NULL


Table: orders
Purpose: Represents customer purchase events.

Columns:
- id: INTEGER, Primary Key
- customer_id: INTEGER, Foreign Key -> customers.id
- order_date: DATE, NOT NULL
- status: VARCHAR(100), NOT NULL


Table: order_items
Purpose: Stores individual items purchased in an order.

Columns:
- id: INTEGER, Primary Key
- order_id: INTEGER, Foreign Key -> orders.id
- product_id: INTEGER, Foreign Key -> products.id
- quantity: INTEGER, NOT NULL
- unit_price: NUMERIC(10,2), NOT NULL

Important:
- Revenue is NOT stored directly in any table.
- Revenue must be calculated as quantity * unit_price.
- Only completed orders should be included when calculating revenue.

"""

if __name__ == "__main__":
    res = get_schema_description()
    print(res);