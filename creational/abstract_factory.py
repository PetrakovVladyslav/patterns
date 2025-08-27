from abc import ABC, abstractmethod


# Абстрактные классы - описывают какие методы должны быть у всех видов оружия и брони
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Armor(ABC):
    @abstractmethod
    def defend(self):
        pass


# Конкретные классы для средневековой темы
class Sword(Weapon):
    def attack(self):
        return "Удар мечом! Урон: 50"


class Shield(Armor):
    def defend(self):
        return "Блок щитом! Защита: 30"


# Конкретные классы для футуристической темы
class LaserGun(Weapon):
    def attack(self):
        return "Выстрел лазером! Урон: 80"


class EnergyShield(Armor):
    def defend(self):
        return "Энергетический щит! Защита: 50"


# Абстрактная фабрика - описывает какие методы должны быть у всех фабрик
class GameFactory(ABC):
    @abstractmethod
    def create_weapon(self):
        pass

    @abstractmethod
    def create_armor(self):
        pass


# Конкретные фабрики для каждой темы
class MedievalFactory(GameFactory):
    def create_weapon(self):
        return Sword()

    def create_armor(self):
        return Shield()


class FuturisticFactory(GameFactory):
    def create_weapon(self):
        return LaserGun()

    def create_armor(self):
        return EnergyShield()


# Класс игры, который использует фабрику
class Game:
    def __init__(self, factory):
        self.factory = factory
        self.weapon = None
        self.armor = None

    def setup_character(self):
        self.weapon = self.factory.create_weapon()
        self.armor = self.factory.create_armor()
        print("Персонаж создан!")

    def battle(self):
        if self.weapon and self.armor:
            print(self.weapon.attack())
            print(self.armor.defend())
        else:
            print("Сначала создай персонажа!")


# Пример использования
if __name__ == "__main__":
    print("=== Средневековая игра ===")
    medieval_factory = MedievalFactory()
    game1 = Game(medieval_factory)
    game1.setup_character()
    game1.battle()

    print("\n=== Футуристическая игра ===")
    futuristic_factory = FuturisticFactory()
    game2 = Game(futuristic_factory)
    game2.setup_character()
    game2.battle()

    print("\n=== Смена темы в процессе игры ===")
    game1.factory = FuturisticFactory()  # Меняем фабрику
    game1.setup_character()  # Создаем нового персонажа
    game1.battle()