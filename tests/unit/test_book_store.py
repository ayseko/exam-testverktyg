from src.book_store import BookStore


def test_add_book():
    book_store = BookStore()
    book_store.addBook("J.K. Rowling", "Harry Potter")
    assert len(book_store.books) == 1

def test_add_multiple_books():
    book_store = BookStore()

    book_store.addBook("J.K. Rowling", "Harry Potter")
    book_store.addBook("Astrid Lindgren", "Pippi Långstrump")

    assert len(book_store.books) == 2

def test_add_book_saves_correct_details():
    book_store = BookStore()

    book_store.addBook("J.K. Rowling", "Harry Potter")

    assert book_store.books[0]["author"] == "J.K. Rowling"
    assert book_store.books[0]["title"] == "Harry Potter"

def test_toggle_favorite_adds_book_to_favorites():
    book_store = BookStore()
    book_store.addBook("J.K. Rowling", "Harry Potter")

    book_id = book_store.books[0]["id"]
    book_store.toggleFavorite(book_id)

    assert book_store.books[0]["favorite"] is True


def test_toggle_favorite_removes_book_from_favorites():
    book_store = BookStore()
    book_store.addBook("J.K. Rowling", "Harry Potter")

    book_id = book_store.books[0]["id"]

    book_store.toggleFavorite(book_id)
    book_store.toggleFavorite(book_id)

    assert book_store.books[0]["favorite"] is False

