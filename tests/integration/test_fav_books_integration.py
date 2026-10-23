
from src.book_store import BookStore
from src.fav_books import FavoriteBooks


def test_added_book_can_be_saved_in_favorite_books():
    book_store = BookStore()
    favorite_books = FavoriteBooks()

    book_store.addBook("J.K. Rowling", "Harry Potter")
    book = book_store.books[0]

    favorite_books.add(book)

    assert book in favorite_books.books
    assert favorite_books.books[0]["title"] == "Harry Potter"
