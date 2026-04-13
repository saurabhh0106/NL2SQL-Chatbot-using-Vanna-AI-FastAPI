import sqlite3

def create_database():
    conn = sqlite3.connect("data/sample.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        name TEXT,
        total_purchase FLOAT
    )
    """)

    cursor.execute("DELETE FROM customers")

    cursor.execute("INSERT INTO customers VALUES (1, 'Saurabh', 5000)")
    cursor.execute("INSERT INTO customers VALUES (2, 'Rahul', 7000)")
    cursor.execute("INSERT INTO customers VALUES (3, 'Amit', 3000)")
    cursor.execute("INSERT INTO customers VALUES (4, 'Neha', 9000)")
    cursor.execute("INSERT INTO customers VALUES (5, 'Priya', 8500)")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
