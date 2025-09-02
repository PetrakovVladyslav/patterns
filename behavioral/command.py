from abc import ABC, abstractmethod

# интерфейс команды - comand
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# получатель команд - receiver, логика внутри класса
class Light:
    def __init__(self, location):
        self.location = location
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"Свет в {self.location} включен")

    def turn_off(self):
        self.is_on = False
        print(f"Свет в {self.location} выключен")


# конкретные команды - concretecommand,
class TurnOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class TurnOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


# инвокер - пульт управления, управляет командами
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()
        else:
            print("Команда не установлена")



if __name__ == "__main__":
 # создаем устройство
    living_room_light = Light("гостиной")

# создаем команды
    turn_on = TurnOnCommand(living_room_light)
    turn_off = TurnOffCommand(living_room_light)

# создаем пульт
    remote = RemoteControl()

    print("Умный дом")

    remote.set_command(turn_on)
    remote.press_button()

    remote.set_command(turn_off)
    remote.press_button()

    remote.set_command(turn_on)
    remote.press_button()