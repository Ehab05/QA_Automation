from API_test_project_part_b.fake_rest_api_data_base.library_data_base import LibraryDataBase


class AuthorEntity(LibraryDataBase):
    def __init__(self, db_name):
        super().__init__(db_name)

    def insert_author(self, author_id_book, author_first_name, author_last_name, table_name):
        self._cursor.execute(f"INSERT INTO {table_name} (author_id_book, author_first_name, author_last_name)"
                             " VALUES (?, ?, ?)", (author_id_book, author_first_name, author_last_name))

    def get_all_authors(self, table_name):
        return self.cursor().execute(f"SELECT * FROM {table_name}")

    def get_author_by_id(self, table_name, author_id):
        return self.cursor().execute(f"SELECT {author_id} FROM {table_name}")

    def update_author_by_id(self, table_name, author_id, author_details):
        columns = ', '.join([f"{key} = ?" for key in author_details.keys()])
        value = author_id + list(author_details.values())
        query = f"UPDATE {table_name} SET {columns} WHERE id= ?"
        self._cursor.execute(query, value)

    def delete_author_by_id(self, author_id, table_name):
        self._cursor.execute(f"'DELETE FROM {table_name} WHERE id = {author_id}'")
