from abc import ABC, abstractmethod

#Абстрактный Наблюдатель, интерфейс для всех подписчиков
class Observer(ABC):
    @abstractmethod
    def update(self, price: float, old_price: float) -> None:
        pass

#Издатель, хранит текущий курс, список подписчиков, добавляет удаляет сабов, метод изменяющий курс
class BitcoinPublisher:
    def __init__(self, initial_price: float):
        self._price = initial_price
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def set_price(self, new_price: float):
        if new_price != self._price:
            old_price = self._price
            print(f"\n[Издатель] Курс Bitcoin изменился: {old_price} → {new_price}")
            self._price = new_price
            self.notify(new_price, old_price)

    def notify(self, price: float, old_price: float):
        for observer in self._observers:
            observer.update(price, old_price)

#наблюдатель
class FallSubscriber(Observer):
    def update(self, price: float, old_price: float):
        if price < old_price:
            print(f"Подписчик на падение: курс упал до {price}$")

#наблюдатель
class RiseSubscriber(Observer):
    def update(self, price: float, old_price: float):
        if price > old_price:
            print(f" Подписчик на рост: курс вырос до {price}$")


if __name__ == "__main__":
    bitcoin = BitcoinPublisher(50000)

    fall_sub = FallSubscriber()
    rise_sub = RiseSubscriber()

    bitcoin.attach(fall_sub)
    bitcoin.attach(rise_sub)


    bitcoin.set_price(51000)
    bitcoin.set_price(49000)
    bitcoin.set_price(49500)
    bitcoin.set_price(49500)
    bitcoin.set_price(48000)
