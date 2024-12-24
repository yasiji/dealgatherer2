import sqlite3

# Connect to the database
conn = sqlite3.connect('../database/deals.db')
cursor = conn.cursor()

# Query all rows from the 'deals' table
cursor.execute('SELECT * FROM deals')
rows = cursor.fetchall()

# Print the rows
for row in rows:
    print(row)

conn.close()
