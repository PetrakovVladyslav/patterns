from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Armor(ABC):
    @abstractmethod
    def defend(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "Удар мечом!"

class Shield(Armor):
    def defend(self):
        return "Блок щитом!"


class LaserGun(Weapon):
    def attack(self):
        return "Выстрел лазером!"

class EnergyShield(Armor):
    def defend(self):
        return "Энергетический щит!"


class GameFactory(ABC):
    @abstractmethod
    def create_weapon(self):
        pass

    @abstractmethod
    def create_armor(self):
        pass


class MedievalFactory(GameFactory):
    def create_weapon(self):
        return Sword()

    def create_armor(self):
        return Shield()

class FantasyFactory(GameFactory):
    def create_weapon(self):
        return LaserGun()

    def create_armor(self):
        return EnergyShield()

class Game:
    def __init__(self, factory):
        self.factory = factory
        self.weapon = None
        self.armor = None

    def setup_character(self):
        self.weapon = self.factory.create_weapon()
        self.armor = self.factory.create_armor()
        print("Персонаж создан")

    def battle(self):
        if self.weapon and self.armor:
            print(self.weapon.attack())
            print(self.armor.defend())


if __name__ == "__main__":
    print("Средневековая игра ")
    medieval_factory = MedievalFactory()
    game1 = Game(medieval_factory)
    game1.setup_character()
    game1.battle()

    print("\nФентези")
    fantasy_factory = FantasyFactory()
    game2 = Game(fantasy_factory)
    game2.setup_character()
    game2.battle()

    print("\nСмена темы в процессе игры")
    game1.factory = FantasyFactory()
    game1.setup_character()
    game1.battle()