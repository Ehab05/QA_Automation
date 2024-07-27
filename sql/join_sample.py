import sqlite3

# Connect to a database (or create it)
conn = sqlite3.connect('example.db')

# Create a cursor object
cur = conn.cursor()

# Clean tables
cur.execute("DELETE from authors")
cur.execute("DELETE from books")

# Create authors table
cur.execute('''
    CREATE TABLE IF NOT EXISTS authors (
        author_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
''')

# Create books table
cur.execute('''
    CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY,
        author_id INTEGER,
        title TEXT,
        FOREIGN KEY (author_id) REFERENCES authors(author_id)
    )
''')

# Commit changes
conn.commit()

# Insert sample data into authors table
cur.execute("INSERT INTO authors (name) VALUES ('J.K. Rowling')")
cur.execute("INSERT INTO authors (name) VALUES ('George R.R. Martin')")

cur.execute("select * from authors")

print("Authors table")
rows = cur.fetchall()
for row in rows:
    print(row)

# Insert sample data into books table
cur.execute("INSERT INTO books (author_id, title) VALUES (1, 'Harry Potter')")
cur.execute("INSERT INTO books (author_id, title) VALUES (2, 'A Game of Thrones')")

cur.execute("select * from books")
print("Books table")
rows = cur.fetchall()
for row in rows:
    print(row)

# Commit changes
conn.commit()

# Perform an INNER JOIN to fetch author names and their book titles
cur.execute('''
    SELECT authors.name, books.title
    FROM authors
    INNER JOIN books ON authors.author_id = books.author_id
''')


# Fetch all results
rows = cur.fetchall()

print("Join")

# Print the results
for row in rows:
    print(f"Author: {row[0]}, Book: {row[1]}")

# Close the connection
conn.close()
