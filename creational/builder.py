'''from abc import ABC, abstractmethod
class Weapon:
    def __init__(self):
        self.parts = []
        self.damage = 0

    def add_part(self, part):
        self.parts.append(part)

    def add_damage(self, damage):
        self.damage += damage

    def __str__(self):
        return f"Оружие: {', '.join(self.parts)} (Урон: {self.damage})"

class WeaponBuilder(ABC):
    @abstractmethod
    def add_base(self): pass

    @abstractmethod
    def add_core_part(self): pass

    @abstractmethod
    def add_enchantment(self): pass

    @abstractmethod
    def get_result(self): pass

class SwordBuilder(WeaponBuilder):
    def __init__(self):
        self.weapon = Weapon()

    def add_base(self):
        self.weapon.add_part("стальная рукоять")
        self.weapon.add_damage(5)

    def add_core_part(self):
        self.weapon.add_part("острое лезвие")
        self.weapon.add_damage(15)

    def add_enchantment(self):
        self.weapon.add_part("руны огня")
        self.weapon.add_damage(10)

    def get_result(self):
        return self.weapon

class BowBuilder(WeaponBuilder):
    def __init__(self):
        self.weapon = Weapon()

    def add_base(self):
        self.weapon.add_part("дубовая основа")
        self.weapon.add_damage(3)

    def add_core_part(self):
        self.weapon.add_part("тетива из жил")
        self.weapon.add_damage(12)

    def add_enchantment(self):
        self.weapon.add_part("магические стрелы")
        self.weapon.add_damage(8)

    def get_result(self):
        return self.weapon

class StaffBuilder(WeaponBuilder):
    def __init__(self):
        self.weapon = Weapon()

    def add_base(self):
        self.weapon.add_part("древесина ивы")
        self.weapon.add_damage(2)

    def add_core_part(self):
        self.weapon.add_part("кристалл маны")
        self.weapon.add_damage(18)

    def add_enchantment(self):
        self.weapon.add_part("заклинание усиления")
        self.weapon.add_damage(12)

    def get_result(self):
        return self.weapon

class WeaponDirector:
    def __init__(self, builder: WeaponBuilder):
        self.builder = builder

    def craft_weapon(self):
        self.builder.add_base()
        self.builder.add_core_part()
        self.builder.add_enchantment()
        return self.builder.get_result()


if __name__ == "__main__":

    sword_builder = SwordBuilder()
    director = WeaponDirector(sword_builder)
    sword = director.craft_weapon()

    bow_builder = BowBuilder()
    director = WeaponDirector(bow_builder)
    bow = director.craft_weapon()

    staff_builder = StaffBuilder()
    director = WeaponDirector(staff_builder)
    staff = director.craft_weapon()

    print(sword)
    print(bow)
    print(staff)


'''
from abc import ABC, abstractmethod

class Weapon:
    def __init__(self):
        self.parts = []
        self.damage = 0

    def add_part(self, part):
        self.parts.append(part)

    def add_damage(self, damage):
        self.damage += damage

    def __str__(self):
        return f"Оружие: {', '.join(self.parts)} (Урон: {self.damage})"

class WeaponBuilder(ABC):
    @abstractmethod
    def add_base(self): pass

    @abstractmethod
    def add_blade(self): pass

    @abstractmethod
    def add_enchantment(self): pass

    @abstractmethod
    def get_result(self): pass


class SwordBuilder(WeaponBuilder):
    def __init__(self):
        self.weapon = Weapon()

    def add_base(self):
        self.weapon.add_part("стальная рукоять")
        self.weapon.add_damage(5)
        return self

    def add_blade(self):
        self.weapon.add_part("острое лезвие")
        self.weapon.add_damage(15)
        return self

    def add_enchantment(self):
        self.weapon.add_part("руны")
        self.weapon.add_damage(10)
        return self

    def get_result(self):
        return self.weapon

class BowBuilder(WeaponBuilder):
    def __init__(self):
        self.weapon = Weapon()

    def add_base(self):
        self.weapon.add_part("дубовая основа")
        self.weapon.add_damage(3)
        return self

    def add_blade(self):
        self.weapon.add_part("тетива")
        self.weapon.add_damage(12)
        return self

    def add_enchantment(self):
        self.weapon.add_part("магические стрелы")
        self.weapon.add_damage(8)
        return self

    def get_result(self):
        return self.weapon

class StaffBuilder(WeaponBuilder):
    def __init__(self):
        self.weapon = Weapon()

    def add_base(self):
        self.weapon.add_part("древесина")
        self.weapon.add_damage(2)
        return self

    def add_blade(self):
        self.weapon.add_part("кристалл")
        self.weapon.add_damage(18)
        return self

    def add_enchantment(self):
        self.weapon.add_part("заклинание")
        self.weapon.add_damage(12)
        return self

    def get_result(self):
        return self.weapon


if __name__ == "__main__":

    full_sword = SwordBuilder().add_base().add_blade().add_enchantment().get_result()

    simple_sword = SwordBuilder().add_base().add_blade().get_result()

    sword_handle = SwordBuilder().add_base().get_result()

    basic_bow = BowBuilder().add_base().add_blade().get_result()

    print("Полное оружие:")
    print(full_sword)
    print("\nНеполное оружие:")
    print(simple_sword)
    print(sword_handle)
    print(basic_bow)
