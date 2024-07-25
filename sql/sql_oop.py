import sqlite3


class SchoolDataBase:
    def __init__(self, db_name):
        self._connection = sqlite3.connect(db_name)
        self._cursor = self._connection.cursor()

    def create_student_table(self, table_name):
        self._cursor.execute(f"'CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, name TEXT NOT NULL, "
                             f"grade INTEGER NOT NULL'")

    def select_from_table(self, table_name, column=None):
        if column:
            self._cursor.execute(f"SELECT {column} FROM {table_name}")
        else:
            self._cursor.execute(f"SELECT * FROM {table_name}")

    def insert_student(self, student_name, student_grade):
        self._cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", (student_name, student_grade))

    def update_student_by_name(self, student_name, student_grade):
        self._cursor.execute(f"'UPDATE students SET grade = {student_grade} WHERE name = {student_name}'")

    def delete_student_by_name(self, student_name):
        self._cursor.execute(f"'DELETE FROM students WHERE name = {student_name}'")

    def get_grade_in_range(self, table_name, grade_range: tuple):
        min_grade, max_grade = grade_range
        self._cursor.execute(f"SELECT * FROM {table_name} WHERE grade > {min_grade} and grade < {max_grade}")

    def print_table(self, table_name):
        self._cursor.execute(f"SELECT * FROM {table_name}")
        rows = self._cursor.fetchall()
        for row in rows:
            print(row)

    def commit_changes(self):
        self._connection.commit()
