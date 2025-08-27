from abc import ABC, abstractmethod

class InventoryItem(ABC):
    @abstractmethod
    def get_weight(self):
        pass

    @abstractmethod
    def show(self, indent=0):
        pass

class Sword(InventoryItem):
    def get_weight(self):
        return 5

    def show(self, level=0):
        return "  " * level + "Меч (5 кг)"

class Potion(InventoryItem):
    def get_weight(self):
        return 1

    def show(self, level=0):
        return "  " * level + "Зелье (1 кг)"

class Gold(InventoryItem):
    def __init__(self, amount):
        self.amount = amount

    def get_weight(self):
        return self.amount * 0.1

    def show(self, level=0):
        return "  " * level + f"Золото x{self.amount} ({self.get_weight()} кг)"

class Bag(InventoryItem):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def get_weight(self):
        return 2 + sum(item.get_weight() for item in self.items)  # сумка весит 2 кг

    def show(self, level=0):
        result = "  " * level + f"{self.name} ({self.get_weight()} кг):\n"
        for item in self.items:
            result += item.show(level + 1) + "\n"
        return result.rstrip()


sword = Sword()
potion1 = Potion()
potion2 = Potion()
gold = Gold(50)

potion_bag = Bag("Сумка зелий")
potion_bag.add(potion1)
potion_bag.add(potion2)

main_bag = Bag("Главный рюкзак")
main_bag.add(sword)
main_bag.add(gold)
main_bag.add(potion_bag)

print(main_bag.show())
print(f"\nОбщий вес: {main_bag.get_weight()} кг")