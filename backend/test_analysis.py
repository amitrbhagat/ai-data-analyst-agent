from app.services.analysis_service import(
    get_total_revenue,
    get_monthly_revenue,
    get_top_products,
    get_top_regions,
    get_average_order_value,
)


print("Total Revenue:")
print(get_total_revenue())

print("\nMonthly Revenue:")
print(get_monthly_revenue())

print("\nTop Products:")
print(get_top_products())

print("\nTop Regions:")
print(get_top_regions())

print("\nAverage Order Value:")
print(get_average_order_value())
