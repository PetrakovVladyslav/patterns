from abc import ABC, abstractmethod

class DamageType(ABC):
    @abstractmethod
    def deal_damage(self, amount):
        pass

class FireDamage(DamageType):
    def deal_damage(self, amount):
        return f"Огненный урон: {amount}"

class IceDamage(DamageType):
    def deal_damage(self, amount):
        return f"Ледяной урон: {amount}"

class PoisonDamage(DamageType):
    def deal_damage(self, amount):
        return f"Ядовитый урон: {amount}"

class Weapon(ABC):
    def __init__(self, damage_type):
        self.damage_type = damage_type  # Мост к реализации

    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return f"Удар мечом! {self.damage_type.deal_damage(30)}"

class Bow(Weapon):
    def attack(self):
        return f"Выстрел из лука! {self.damage_type.deal_damage(20)}"

class Staff(Weapon):
    def attack(self):
        return f"Заклинание посохом! {self.damage_type.deal_damage(40)}"

fire_sword = Sword(FireDamage())
ice_bow = Bow(IceDamage())
poison_staff = Staff(PoisonDamage())

fire_bow = Bow(FireDamage())
ice_sword = Sword(IceDamage())

weapons = [fire_sword, ice_bow, poison_staff, fire_bow, ice_sword]

for weapon in weapons:
    print(weapon.attack())