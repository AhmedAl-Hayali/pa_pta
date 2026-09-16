import sqlite3

def get_customer_spend():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Join Customers, Orders, and Order_Items to calculate 
    # total spend (price * quantity) per Customer Name.
    query = """
    SELECT c.name, SUM(oi.price * oi.quantity) AS spend
    FROM Customers AS c
    JOIN Orders AS o
    ON c.customer_id = o.customer_id
    JOIN Order_items AS oi
    ON o.order_id = oi.order_id
    GROUP BY c.name;
    """
    
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

print(get_customer_spend())