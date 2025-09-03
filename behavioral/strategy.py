from abc import ABC, abstractmethod

# Абстрактная стратегия
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Конкретные стратегии
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Оплачено {amount} грн картой"


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Оплачено {amount} грн через PayPal"


class CashPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Оплачено {amount} грн наличными"


# Контекст, хранит текущую стратегию черещ _payment_strategy
class ShoppingCart:
    def __init__(self):
        self._payment_strategy = None

    def set_payment_strategy(self, strategy):
        self._payment_strategy = strategy

#метод делегирует оплату выбранной стратегии
    def checkout(self, amount):
        if self._payment_strategy:
            return self._payment_strategy.pay(amount)
        return "Не выбран способ оплаты"



if __name__ == "__main__":
    cart = ShoppingCart()

    cart.set_payment_strategy(CreditCardPayment())
    print(cart.checkout(1000))


    cart.set_payment_strategy(PayPalPayment())
    print(cart.checkout(1500))


    cart.set_payment_strategy(CashPayment())
    print(cart.checkout(500))