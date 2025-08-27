from abc import ABC, abstractmethod


class Character(ABC):
    @abstractmethod
    def get_damage(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

class Warrior(Character):
    def get_damage(self):
        return 20

    def get_description(self):
        return "Воин"


class Equipment(Character):
    def __init__(self, character):
        self._character = character

    def get_damage(self):
        return self._character.get_damage()

    def get_description(self):
        return self._character.get_description()

class Sword(Equipment):
    def get_damage(self):
        return self._character.get_damage() + 15

    def get_description(self):
        return self._character.get_description() + " + Меч"

class Shield(Equipment):
    def get_damage(self):
        return self._character.get_damage() + 5

    def get_description(self):
        return self._character.get_description() + " + Щит"


warrior = Warrior()
print(f"{warrior.get_description()}: урон {warrior.get_damage()}")

warrior_with_sword = Sword(warrior)
print(f"{warrior_with_sword.get_description()}: урон {warrior_with_sword.get_damage()}")

warrior_with_sword_shield = Shield(warrior_with_sword)
print(f"{warrior_with_sword_shield.get_description()}: урон {warrior_with_sword_shield.get_damage()}")

warrior_with_shield = Shield(warrior)
print(f"{warrior_with_shield.get_description()}: урон {warrior_with_shield.get_damage()}")

