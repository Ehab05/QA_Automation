import json
import webbrowser
from urllib.parse import urlencode
from Book import Book


class Library:
    def __init__(self, library_file):
        self.books = None  # for the first time use of the app the list will be empty
        self.library_file = library_file
        self.load_library()

    def load_library(self):
        try:
            # Attempt to open the JSON file specified by self.library_file
            with open(self.library_file, 'r') as file:
                # Load JSON data from the file and convert each object to a Book instance
                self.books = json.load(file, object_hook=lambda d: Book.load_book(d))

        except FileNotFoundError:
            # If the file is not found, handle the exception by setting books to an empty
            self.books = []

    def save_library(self):
        # Open the file specified by self.library_file in write mode ('w')
        with open(self.library_file, 'w') as file:
            # Convert self.books (list of Book objects) to JSON and write to the file
            json.dump(self.books, file, default=lambda obj: obj.__dict__, indent=4)

    # This function adds a book the library and then save the changes
    def add_book(self, book):
        self.books.append(book)
        self.save_library()

    # this function display all the saved books in the library
    def list_books(self):
        return self.books

    # this function search for a book by its author
    def find_books_by_author(self, author):
        return [book for book in self.books if author.lower() in book.author.lower()]

    # this function search for a book by its title
    def find_books_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    # this function deletes a book from the library
    def delete_book(self, title):
        initial_count = len(self.books)
        self.books = [book for book in self.books if book.title != title]
        if len(self.books) < initial_count:
            self.save_library()
            return True
        return False

    # this function directs the user to google books search
    def search_online(self, query):
        search_url = 'https://books.google.com'
        params = {'q': query}
        # Construct the full URL with query parameters
        url = search_url + '?' + urlencode(params)
        webbrowser.open(url)
