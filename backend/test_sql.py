from app.schemas.sql import SQLGenerationResult


result = SQLGenerationResult(
    sql= "SELECT SUM(quantity * unit_price) FROM order_items ...",
    reasoning_summary= "Calculates revenue from completed orders.",
    confidence= 0.92
)

print(result)