import sqlite3

# Connect to a database (or create it)
conn = sqlite3.connect('example.db')

# Create a cursor object
cur = conn.cursor()

cur.execute('DROP TABLE users')
# Execute SQL commands
cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')

# Commit changes and close the connection
conn.commit()
conn.close()
