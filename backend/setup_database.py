import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('../database/deals.db')
cursor = conn.cursor()

# Create the deals table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS deals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        price TEXT NOT NULL,
        retailer TEXT NOT NULL,
        link TEXT NOT NULL
    )
''')

conn.commit()
conn.close()

print("Database setup complete.")
