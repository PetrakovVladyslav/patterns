
class CoinType:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def show(self, x, y):
        print(f"{self.color} монета ({self.value} золота) в позиции ({x}, {y})")


coin_types = {}

def get_coin_type(value, color):
    key = (value, color)
    if key not in coin_types:
          coin_types[key] = CoinType(value, color)
    return coin_types[key]


class Coin:
    def __init__(self, x, y, value, color):
        self.x = x
        self.y = y
        self.coin_type = get_coin_type(value, color)

    def show(self):
        self.coin_type.show(self.x, self.y)

coins = []
coins.append(Coin(10, 20, 1, "медная"))
coins.append(Coin(30, 40, 5, "серебряная"))
coins.append(Coin(50, 60, 1, "медная"))
coins.append(Coin(70, 80, 1, "медная"))
coins.append(Coin(90, 100, 5, "серебряная"))

print("Монеты на карте:")
for coin in coins:
    coin.show()

print(f"\nВсего монет: {len(coins)}")
print(f"Типов монет: {len(coin_types)}")