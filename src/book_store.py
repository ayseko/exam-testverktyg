
class BookStore:
    def __init__(self):
        self.books = []

    def addBook(self, author, title):
        book = {
            "id": len(self.books) + 1,
            "author": author,
            "title": title,
            "favorite": False
        }
        self.books.append(book)

    def toggleFavorite(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                book["favorite"] = not book["favorite"]
                return