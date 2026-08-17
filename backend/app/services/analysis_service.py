import pandas as pd

from app.database.connection import engine



def get_total_revenue():
    query = """
        SELECT
            COALESCE(SUM(oi.quantity * oi.unit_price), 0) AS total_revenue
        FROM order_items oi
        JOIN orders o
            ON o.id = oi.order_id
        WHERE o.status = 'completed';
    """

    result = pd.read_sql(query, engine)

    return result.iloc[0]["total_revenue"]


def get_monthly_revenue():
    query = """
        SELECT
            DATE_TRUNC('month', o.order_date) AS month,
            SUM(oi.quantity * oi.unit_price) AS revenue
        FROM order_items oi
        JOIN orders o
            ON o.id = oi.order_id
        WHERE o.status = 'completed'
        GROUP BY DATE_TRUNC('month', o.order_date)
        ORDER BY month;
    """

    return pd.read_sql(query, engine)


def get_top_products(limit=5):
    query = """
        SELECT
            p.id AS product_id,
            p.name AS product_name,
            SUM(oi.quantity * oi.unit_price) AS revenue
        FROM order_items oi
        JOIN orders o
            ON o.id = oi.order_id
        JOIN products p
            ON p.id = oi.product_id
        WHERE o.status = 'completed'
        GROUP BY p.id, p.name
        ORDER BY revenue DESC
        LIMIT %(limit)s;
    """

    return pd.read_sql(query, engine, params={"limit": limit})


def get_top_regions(limit=5):
    query = """
        SELECT
            r.id AS region_id,
            r.name AS region_name,
            SUM(oi.quantity * oi.unit_price) AS revenue
        FROM regions r
        JOIN customers c
            ON c.region_id = r.id
        JOIN orders o
            ON o.customer_id = c.id
        JOIN order_items oi
            ON oi.order_id = o.id
        WHERE o.status = 'completed'
        GROUP BY r.id, r.name
        ORDER BY revenue DESC
        LIMIT %(limit)s;
    """

    return pd.read_sql(query, engine, params={"limit": limit})


def get_average_order_value():
    query = """
        SELECT
            COALESCE(AVG(order_revenue), 0) AS average_order_value
        FROM (
            SELECT
                o.id AS order_id,
                SUM(oi.quantity * oi.unit_price) AS order_revenue
            FROM orders o
            JOIN order_items oi
                ON oi.order_id = o.id
            WHERE o.status = 'completed'
            GROUP BY o.id
        ) order_totals;
    """

    result = pd.read_sql(query, engine)

    return result.iloc[0]["average_order_value"]

