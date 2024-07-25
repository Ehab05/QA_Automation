import sqlite3

connection = sqlite3.connect('school.db')

cursor = connection.cursor()
# Creating the table
cursor.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)')
# Inserting the values
student_1 = 'Ehab'
student_1_grade = 87
student_2 = 'Majd'
student_2_grade = 90
student_3 = 'Shakeed'
student_3_grade = 78

cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", (student_1, student_1_grade))
cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", (student_2, student_2_grade))
cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", (student_3, student_3_grade))
print("Students with a grade higher than 80")
# Printing the students with the grade that higher than 80
cursor.execute("SELECT * FROM students WHERE grade > 80")
rows = cursor.fetchall()
for row in rows:
    print(row)
# Updating student grade and deleting another
cursor.execute("UPDATE students SET grade = 85.5 WHERE name = 'Ehab'")
cursor.execute("DELETE FROM students WHERE name = 'Majd'")
print("\nAfter updating Ehabs grade and deleting Majd")
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

connection.commit()
cursor.close()



