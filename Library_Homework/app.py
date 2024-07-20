from urllib import request
from flask import Flask, render_template, request, redirect, url_for, flash
from Book import Book
from Library import Library
import secrets

secret_key = secrets.token_hex(16)
app = Flask(__name__)
app.secret_key = secret_key
library = Library("library.json")


# this route is fot the home page
@app.route('/')
def home():
    return render_template('home.html')


# this route displays all the books in the library
@app.route('/list')
def list_books():
    books = library.list_books()
    return render_template('book_list.html', books=books)


# this route for adding books
@app.route('/add', methods=['GET', 'POST'])
def add_book():
    try:
        if request.method == 'POST':
            title = request.form['title']
            author = request.form['author']
            publication_year = request.form['publication_year']
            genre = request.form['genre']

            if not title or not author or not publication_year or not genre:
                flash("All fields are required.")
                return redirect(url_for('add_book'))

            try:
                publication_year = int(publication_year)
            except ValueError:
                flash("Publication year must be a number.")
                return redirect(url_for('add_book'))

            if not genre.isalpha():
                flash("Genre must contain only letters.")
                return redirect(url_for('add_book'))

            book = Book(title, author, publication_year, genre)
            library.add_book(book)
            return redirect(url_for('list_books'))

    except Exception as e:
        app.logger.error(f"Error adding book: {e}")
        flash("An error occurred while adding the book.")
        return redirect(url_for('add_book'))

    return render_template('add_book.html')


@app.route('/delete', methods=['GET', 'POST'])
def delete_book():
    if request.method == 'POST':
        selected_title = request.form.get('book_title')  # Get selected book title from form
        if selected_title:
            # Check if 'confirm_delete' is in request.form
            if 'confirm_delete' in request.form:
                confirm_delete = request.form['confirm_delete']
                if confirm_delete == 'yes':
                    # Perform deletion logic here
                    if library.delete_book(selected_title):
                        flash(f"Book '{selected_title}' has been deleted.", 'success')
                        return redirect(url_for('list_books'))
                    else:
                        flash(f"Failed to delete book '{selected_title}'.", 'error')
                        return redirect(url_for('list_books'))
                else:
                    flash("Deletion not confirmed.", 'error')
                    return redirect(url_for('list_books'))

            # Render the delete book confirmation page if 'confirm_delete' not in request.form
            return render_template('delete_confirmation.html', book_title=selected_title)

    # Render the delete book selection page (GET request or initial render)
    all_books = library.books
    return render_template('delete_book.html', all_books=all_books)


# Route to search books by author
@app.route('/search/author', methods=['GET', 'POST'])
def search_by_author():
    if request.method == 'POST':
        author = request.form['author']
        books = library.find_books_by_author(author)
        return render_template('search_results.html', books=books, search_type="Author", search_value=author)
    return render_template('search_by_author.html')


# Route to search books by title
@app.route('/search/title', methods=['GET', 'POST'])
def search_by_title():
    if request.method == 'POST':
        title = request.form['title']
        books = library.find_books_by_title(title)
        return render_template('search_results.html', books=books, search_type="Title", search_value=title)
    return render_template('search_by_title.html')


# Route to edit book
@app.route('/edit/<title>', methods=['GET', 'POST'])
def edit_book(title):
    if title == 'choose':
        # Handle book selection
        if request.method == 'POST':
            selected_title = request.form.get('book_title')
            if selected_title:
                return redirect(url_for('edit_book', title=selected_title))
            else:
                flash("Please select a book to edit.", 'error')
        books = library.books  # Get list of books
        return render_template('choose_book.html', books=books)

    # Continue with edit functionality
    book_to_edit = None
    for book in library.books:
        if book.title == title:
            book_to_edit = book
            break

    if not book_to_edit:
        return "Book not found", 404

    if request.method == 'POST':
        # Process form submission to update book details
        new_title = request.form.get('title')
        new_author = request.form.get('author')
        new_year = request.form.get('publication_year')
        new_genre = request.form.get('genre')

        # Update book details if new values are provided
        if new_title:
            book_to_edit.title = new_title
        if new_author:
            book_to_edit.author = new_author
        if new_year:
            try:
                book_to_edit.publication_year = int(new_year)  # Convert year to integer
            except ValueError:
                return "Publication year must be a number.", 400
        if new_genre:
            try:
                book_to_edit.genre = str(new_genre)  # Ensure genre is a string
            except ValueError:
                return "Genre must be a string.", 400

        # Save changes to library
        library.save_library()

        # Redirect to the book list
        return redirect(url_for('list_books'))

    # Render the edit form with the book details pre-filled
    return render_template('edit_book.html', book=book_to_edit)


# Route to search online
@app.route('/search_online', methods=['GET', 'POST'])
def search_online():
    if request.method == 'POST':
        query = request.form['query']
        try:
            manager = Library('library.json')
            manager.search_online(query)
            return redirect(url_for('home'))
        except Exception as e:
            app.logger.error(f"Error searching online: {e}")
            return "An error occurred while searching online. Please try again.", 500
    return render_template('search_online.html')
