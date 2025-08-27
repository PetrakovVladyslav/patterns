import copy
from abc import ABC, abstractmethod

class Enemy(ABC):
    def __init__(self, name, health, damage, speed):
        self.name = name
        self.health = health
        self.damage = damage
        self.speed = speed

    @abstractmethod
    def clone(self):
        pass

    def __str__(self):
        return f"{self.name}: HP={self.health}, Damage={self.damage}, Speed={self.speed}"

class Orc(Enemy):
    def __init__(self, name="Орк", health=100, damage=25, speed=5):
        super().__init__(name, health, damage, speed)
        self.weapon = "Топор"

    def clone(self):
        return copy.deepcopy(self)

class Goblin(Enemy):
    def __init__(self, name="Гоблин", health=60, damage=15, speed=8):
        super().__init__(name, health, damage, speed)
        self.stealth = True

    def clone(self):
        return copy.deepcopy(self)

class Dragon(Enemy):
    def __init__(self, name="Дракон", health=300, damage=50, speed=3):
        super().__init__(name, health, damage, speed)
        self.fire_breath = True
        self.armor = 20

    def clone(self):
        return copy.deepcopy(self)


class EnemyFactory:
    def __init__(self):
        self._prototypes = {}

    def register_prototype(self, name, prototype):
        self._prototypes[name] = prototype

    def create_enemy(self, name):
        if name in self._prototypes:
            return self._prototypes[name].clone()
        return None


def main():
    factory = EnemyFactory()

    factory.register_prototype("orc", Orc())
    factory.register_prototype("goblin", Goblin())
    factory.register_prototype("dragon", Dragon())


    orc1 = factory.create_enemy("orc")
    orc2 = factory.create_enemy("orc")

    goblin1 = factory.create_enemy("goblin")
    dragon1 = factory.create_enemy("dragon")

    orc1.name = "Орк-воин"
    orc1.health = 120

    orc2.name = "Орк-вождь"
    orc2.damage = 35

    goblin1.name = "Гоблин-лучник"
    goblin1.damage = 20

    dragon1.name = "Древний дракон"
    dragon1.health = 500

    enemies = [orc1, orc2, goblin1, dragon1]

    for enemy in enemies:
        print(enemy)

if __name__ == "__main__":
    main()