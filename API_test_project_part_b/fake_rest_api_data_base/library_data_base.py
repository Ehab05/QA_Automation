import sqlite3


class LibraryDataBase:
    def __init__(self, db_name):
        self._connection = sqlite3.connect(db_name)
        self._cursor = self._connection.cursor()

    def create_author_table(self):
        # Creating a new author table with the given name
        self._cursor.execute(
            '''CREATE TABLE IF NOT EXISTS author
            (id INTEGER PRIMARY KEY, idBook INTEGER NOT NULL, firstName TEXT NOT NULL, 
            lastName TEXT NOT NULL)''')
        self.commit_changes()

    def create_book_table(self):
        return self._cursor.execute('''CREATE TABLE IF NOT EXISTS book
                                        (id_key INTEGER PRIMARY KEY, id INTEGER, title TEXT NOT NULL, 
                                        description TEXT NOT NULL, pageCount INTEGER NOT NULL,
                                       excerpt TEXT NOT NULL, publishDate DATE NOT NULL''')

    def cursor(self):
        return self._cursor

    def select_table(self, table_name):
        return self._cursor.execute(f"SELECT * FROM {table_name}")

    def select_column_from_table(self, table_name, column=None):
        return self._cursor.execute(f"SELECT {column} FROM {table_name}")

    def create_index(self, index_name, table_name, column_name):
        self._cursor.execute(f"CREATE INDEX IF NOT EXISTS {index_name} ON {table_name} ({column_name})")
        self._connection.commit()

    def commit_changes(self):
        self._connection.commit()
