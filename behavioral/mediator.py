from abc import ABC, abstractmethod

# абстрактный посредник, определяет интерфейс прспрелнеика - метода request_runway
class TrafficController(ABC):
    @abstractmethod
    def request_runway(self, aircraft: 'Aircraft') -> None:
        pass

# Конкретный посредник runway_busy - request_runway проверяет этот флаг занята ли полоса, он реализуеит интерфейс абстрактного посредника
#
class Airport(TrafficController):
    def __init__(self):
        self.runway_busy = False

    def request_runway(self, aircraft: 'Aircraft') -> None:
        if self.runway_busy:
            print(f"{aircraft.name}: Полоса занята")
            aircraft.wait()
        else:
            print(f"{aircraft.name}: Полоса свободна")
            self.runway_busy = True
            aircraft.use_runway()
            self.runway_busy = False


# Абстрактный коллега, базовый класс для всех типов коллег(самолетов), содержит имя и ссыоку на диспетчера
#Aircraft объявляет два абстрактных метода use_runway и wait, которые реализуются в подклассах
class Aircraft(ABC):
    def __init__(self, name: str, controller: TrafficController):
        self.name = name
        self.controller = controller

    def request_landing(self) -> None:
        self.controller.request_runway(self)

    @abstractmethod
    def use_runway(self) -> None:
        pass

    @abstractmethod
    def wait(self) -> None:
        pass


# Конкретные коллеги
class PassengerPlane(Aircraft):
    def use_runway(self) -> None:
        print(f"{self.name} приземлился")

    def wait(self) -> None:
        print(f"{self.name} ожидает")


class CargoPlane(Aircraft):
    def use_runway(self) -> None:
        print(f"{self.name} приземлился")

    def wait(self) -> None:
        print(f"{self.name} ожидает")


if __name__ == "__main__":
    airport = Airport()

    plane1 = PassengerPlane("SU", airport)
    plane2 = CargoPlane("Boing", airport)

    plane1.request_landing()
    plane2.request_landing()  # ВПП занята