from abc import ABC, abstractmethod


#  абстрактный интерфейс
class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


#Конкретные элементы
class Book(Element):
    def accept(self, visitor):
        visitor.visit_book(self)

    def get_price(self):
        return 10


class Fruit(Element):
    def accept(self, visitor):
        visitor.visit_fruit(self)

    def get_price(self):
        return 5


#Интерфейс посетителя
class Visitor(ABC):
    @abstractmethod
    def visit_book(self, book):
        pass

    @abstractmethod
    def visit_fruit(self, fruit):
        pass


#онкретный посетитель
class DiscountVisitor(Visitor):
    def visit_book(self, book):
        print(f"Книга: цена со скидкой {book.get_price() * 0.9}")

    def visit_fruit(self, fruit):
        print(f"Фрукты: цена со скидкой {fruit.get_price() * 0.8}")



if __name__ == "__main__":
    items = [Book(), Fruit()]
    visitor = DiscountVisitor()

    for item in items:
        item.accept(visitor)