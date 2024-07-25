from API_test_project_part_b.fake_rest_api_data_base.library_data_base import LibraryDataBase


class BookEntity(LibraryDataBase):
    def __init__(self, db_name, book):
        super().__init__(db_name)
        self._id = book["id"]
        self._title = book["title"]
        self._description = book["description"]
        self._pageCount = book["pageCount"]
        self._excerpt = book["excerpt"]
        self._publishDate = book["publishDate"]

    def insert_book(self):
        self._cursor.execute("INSERT INTO book (id, title, description, pageCount, excerpt, publishDate) VALUES "
                             "(?, ?, ?, ?, ?)", (self._id, self._title, self._description, self._pageCount,
                                                 self._excerpt, self._publishDate))

    def get_all_books(self):
        return self.cursor().execute("SELECT * FROM book")

    def get_book_by_id(self, book_id):
        return self.cursor().execute(f"SELECT {book_id} FROM book")

    def update_book_by_id(self, book_id, book_details):
        # Create a string for the columns to be updated
        columns = ', '.join([f"{key} = ?" for key in book_details.keys()])

        # Create a list of values to be updated, with book_id at the end
        values = list(book_details.values())
        values.append(book_id)

        # Create the SQL update query
        query = f"UPDATE book SET {columns} WHERE id = ?"

        # Execute the query with the values
        self._cursor.execute(query, values)
        self.commit_changes()

    def delete_book_by_id(self, book_id):
        return self._cursor.execute(f"'DELETE FROM book WHERE id = {book_id}'")
