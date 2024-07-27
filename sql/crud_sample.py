import sqlite3

conn = sqlite3.connect('example.db')
cur = conn.cursor()

# Clean table
cur.execute("DELETE from users")

# Create
cur.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
cur.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")

print("start")
# Read
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)

# Update
cur.execute("UPDATE users SET age = 31 WHERE name = 'Alice'")
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
print("After update")
for row in rows:
    print(row)

# Delete
cur.execute("DELETE FROM users WHERE name = 'Bob'")
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
print("After delete")
for row in rows:
    print(row)

conn.commit()
conn.close()
