
from src.fav_books import FavoriteBooks


def test_add_book_to_favorites():
    favorite_books = FavoriteBooks()
    book = {
        "id": 1,
        "author": "J.K. Rowling",
        "title": "Harry Potter"
    }

    favorite_books.add(book)

    assert book in favorite_books.books

def test_remove_book_from_favorites():
    favorite_books = FavoriteBooks()
    book = {
        "id": 1,
        "author": "J.K. Rowling",
        "title": "Harry Potter"
    }

    favorite_books.add(book)
    favorite_books.remove(book)

    assert book not in favorite_books.books
