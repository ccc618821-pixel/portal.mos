from decimal import Decimal
from services.pricing import calculate_discount_percent, calculate_final_price, get_previous_month_range
CATALOG_QUERY = """
    SELECT p.product_id,
           p.product_name,
           p.category,
           p.subcategory,
           p.image_path,
           p.manufacturer,
           p.description,
           p.composition,
           p.price,
           COALESCE((SELECT SUM(s.quantity_available)
                     FROM stock_items s
                     WHERE s.product_id = p.product_id), 0) AS total_quantity,
           EXISTS (SELECT 1
                   FROM order_items oi
                   JOIN orders o ON o.order_id = oi.order_id
                   WHERE oi.product_id = p.product_id
                     AND o.order_date >= %s
                     AND o.order_date < %s) AS ordered_last_month
    FROM products p
    ORDER BY p.product_id
"""
def convert_row_to_catalog_item(row):
    base_price = Decimal(str(row[8]))
    discount_percent = calculate_discount_percent(bool(row[10]))
    return {
        "product_id": row[0],
        "product_name": row[1],
        "category": row[2],
        "subcategory": row[3],
        "image_path": row[4] or "",
        "manufacturer": row[5],
        "description": row[6] or "",
        "composition": row[7] or "",
        "base_price": base_price,
        "discount_percent": discount_percent,
        "final_price": calculate_final_price(base_price, discount_percent),
        "total_quantity": int(row[9]),
    }
def fetch_catalog_items(connection, calculation_date):
    previous_month_start, current_month_start = get_previous_month_range(calculation_date)
    cursor = connection.cursor()
    try:
        cursor.execute(CATALOG_QUERY, (previous_month_start, current_month_start))
        rows = cursor.fetchall()
    finally:
        cursor.close()
    return [convert_row_to_catalog_item(row) for row in rows]
