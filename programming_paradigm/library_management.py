# library_management.py

class Book:
    """
    Represents a single book in a library, with a title, author,
    and a status indicating if it is checked out.
    """

    def __init__(self, title, author):
        """Initializes a Book instance."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Marks the book as returned (not checked out)."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is not checked out, False otherwise."""
        return not self._is_checked_out


class Library:
    """
    Represents a library, which manages a collection of Book objects.
    """

    def __init__(self):
        """Initializes a Library instance with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Adds a Book object to the library's collection."""
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        """
        Finds a book by its title and checks it out if it is available.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return

    def return_book(self, title):
        """
        Finds a book by its title and returns it to the library.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return

    def list_available_books(self):
        """
        Prints the title and author of all books that are currently available.
        """
        available_books_found = False
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
                available_books_found = True
        if not available_books_found:
            # This part is not required by the prompt but handles the case
            # where no books are available to list. then pass or go to other services.
            pass
