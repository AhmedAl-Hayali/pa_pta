import sqlite3

def get_popular_skus():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Return SKUs where the SUM of quantity across all orders is > 1.
    query = """
    SELECT sku
    FROM Order_Items AS oi
    --FROM Orders AS o
    --JOIN Order_Items AS oi
    --ON o.order_id = oi.order_id
    GROUP BY sku
      HAVING SUM(oi.quantity) > 1
    """
    
    cursor.execute(query)
    return cursor.fetchall()

print(get_popular_skus())