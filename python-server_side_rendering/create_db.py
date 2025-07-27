import sqlite3

def create_database():
    try:
        # Use a 'with' statement for automatic connection management
        with sqlite3.connect('products.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Products (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    category TEXT NOT NULL,
                    price REAL NOT NULL
                )
            ''')
            cursor.execute('''
                INSERT OR IGNORE INTO Products (id, name, category, price)
                VALUES
                (1, 'Laptop', 'Electronics', 799.99),
                (2, 'Coffee Mug', 'Home Goods', 15.99),
                (3, 'Coffee Mug Puppy', 'Home Goods', 18.99)
            ''')
    except sqlite3.Error as e:
        print(f"Database error: {e}")

if __name__ == '__main__':
    create_database()
