from abc import ABC, abstractmethod

# Абстрактное состояние
class State(ABC):
    @abstractmethod
    def insert_coin(self, machine):
        pass

    @abstractmethod
    def press_button(self, machine):
        pass


class NoCoinState(State):
    def insert_coin(self, machine):
        print("Монета вставлена")
        machine.set_state(machine.has_coin_state)

    def press_button(self, machine):
        print("Сначала вставьте монету")


class HasCoinState(State):
    def insert_coin(self, machine):
        print("Монета уже вставлена")

    def press_button(self, machine):
        print("Товар выдан!")
        machine.set_state(machine.no_coin_state)


# Контекст
class VendingMachine:
    def __init__(self):
 # Создаем состояния
        self.no_coin_state = NoCoinState()
        self.has_coin_state = HasCoinState()

 #Начальное состояние
        self.current_state = self.no_coin_state

    def set_state(self, state):
        self.current_state = state

    def insert_coin(self):
        self.current_state.insert_coin(self)

    def press_button(self):
        self.current_state.press_button(self)



if __name__ == "__main__":
    machine = VendingMachine()

    print("Тест торгового автомата: ")

    machine.press_button()

    machine.insert_coin()

    machine.insert_coin()

    machine.press_button()

    machine.press_button()