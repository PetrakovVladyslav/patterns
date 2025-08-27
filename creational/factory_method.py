from abc import ABC, abstractmethod


class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def __str__(self):
        return f"{self.name} (HP: {self.health}, DMG: {self.damage})"


class Orc(Enemy):
    def __init__(self):
        super().__init__("Орк", 100, 15)

class Goblin(Enemy):
    def __init__(self):
        super().__init__("Гоблин", 50, 8)

class Dragon(Enemy):
    def __init__(self):
        super().__init__("Дракон", 500, 50)


class EnemySpawner(ABC):
    @abstractmethod
    def create_enemy(self) :
        pass

    def spawn(self):
        enemy = self.create_enemy()
        print(f"Появился враг: {enemy}")
        return enemy

class OrcSpawner(EnemySpawner):
    def create_enemy(self):
        return Orc()

class GoblinSpawner(EnemySpawner):
    def create_enemy(self):
        return Goblin()

class DragonSpawner(EnemySpawner):
    def create_enemy(self):
        return Dragon()

if __name__ == "__main__":
    print("СПАВН ВРАГОВ\n")

    orc_spawner = OrcSpawner()
    goblin_spawner = GoblinSpawner()
    dragon_spawner = DragonSpawner()

    orc = orc_spawner.spawn()
    goblin = goblin_spawner.spawn()
    dragon = dragon_spawner.spawn()

    spawners = [orc_spawner, goblin_spawner, dragon_spawner]

    print("\nСлучайные враги:")
    import random

    for i in range(3):
        random_spawner = random.choice(spawners)
        enemy = random_spawner.spawn()
