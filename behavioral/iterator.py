from collections.abc import Iterator, Iterable

# позже добавляем Бук в словарь
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' - {self.author} ({self.year})"


class TitleIterator(Iterator):
    def __init__(self, books):
        self.books = books
        self.index = 0

    def __next__(self):
        if self.index >= len(self.books):
            raise StopIteration
        book = self.books[self.index]
        self.index += 1
        return book.title


class AuthorIterator(Iterator):
    def __init__(self, books):
        self.books = books
        self.index = 0

    def __next__(self):
        if self.index >= len(self.books):
            raise StopIteration
        book = self.books[self.index]
        self.index += 1
        return book.author


class ReverseIterator(Iterator):
    def __init__(self, books):
        self.books = books
        self.index = len(books) - 1

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        book = self.books[self.index]
        self.index -= 1
        return book



class Library(Iterable):
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __iter__(self):
# ро умолчанию  обычный порядок
        return iter(self.books)

    def titles(self):
        return TitleIterator(self.books)

    def authors(self):
        return AuthorIterator(self.books)

    def reverse(self):
        return ReverseIterator(self.books)



if __name__ == "__main__":

    library = Library()
    library.add_book(Book("1984", "Оруэлл", 1949))
    library.add_book(Book("Мастер и Маргарита", "Булгаков", 1967))
    library.add_book(Book("Война и мир", "Толстой", 1869))

    print("Все книги ")
    for book in library:
        print(book)

    print("\nТолько названия")
    for title in library.titles():
        print(f'{title}')

    print("\nТолько авторы")
    for author in library.authors():
      print(f"{author}")

    print("\nВ обратном порядке")
    for book in library.reverse():
      print(f"{book}")