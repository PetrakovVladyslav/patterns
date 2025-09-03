from abc import ABC, abstractmethod


class GameSession(ABC):
#Абстрактный класс

    def play_game(self):
#Шаблонный метод  определяет ход игры
        self.start_game()
        self.play_main_phase()
        self.hook_before_end()
        self.end_game()

    def start_game(self):
        print("Игра начинается")

    def end_game(self):
        print("Игра завершена")

    @abstractmethod
    def play_main_phase(self):
        pass

    def hook_before_end(self):
        pass


class ChessGame(GameSession):

    def play_main_phase(self):
        print("Игроки ходят по очереди фигурами")


class PokerGame(GameSession):

    def play_main_phase(self):
        print("Игроки делают ставки")

    def hook_before_end(self):
        print("Подсчет")


if __name__ == "__main__":
    print("Шахматы")
    ChessGame().play_game()

    print("\nПокер")
    PokerGame().play_game()