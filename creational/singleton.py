class GameManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False  # добавим флаг
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.score = 0
            self.level = 1
            self._initialized = True

    def add_score(self, points):
        self.score += points
        print(f"Счет: {self.score}")

    def next_level(self):
        self.level += 1
        print(f"Уровень: {self.level}")


game1 = GameManager()
game2 = GameManager()

print(f"Один объект? {game1 is game2}")

game1.add_score(100)
game2.next_level()
game2.next_level()
game1.score = 999
game1.add_score(100)
print(f"Счет: {game1.score}")
print(f"Уровень: {game2.level}")

print(f"Один объект? {game1 is game2}")