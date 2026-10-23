
from src.book_store import BookStore


def test_added_book_can_be_marked_as_favorite():
    book_store = BookStore()

    book_store.addBook("J.K. Rowling", "Harry Potter")
    book_id = book_store.books[0]["id"]

    book_store.toggleFavorite(book_id)

    assert book_store.books[0]["title"] == "Harry Potter"
    assert book_store.books[0]["favorite"] is True
