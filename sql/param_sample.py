import sqlite3

conn = sqlite3.connect('example.db')
cur = conn.cursor()

# Clean table
cur.execute("DELETE from users")

# Using parameters
name = 'Charlie'
age = 28
cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))

# Fetching data with a parameter
cur.execute("SELECT * FROM users WHERE age > ?", (25,))
rows = cur.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()
