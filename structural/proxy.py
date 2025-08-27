class Gun:
    def shoot(self):
        print("Выстрел!")

class AmmoProxy:
    def __init__(self, gun):
        self.gun = gun
        self.ammo = 3  # Патроны

    def shoot(self):
        if self.ammo > 0:
            self.ammo -= 1
            self.gun.shoot()  # Стреляем
            print(f"Патронов осталось: {self.ammo}")
        else:
            print("Нет патронов!")


pistol = Gun()
loaded_pistol = AmmoProxy(pistol)

print("Стрельба:")
loaded_pistol.shoot()  # 1-й выстрел
loaded_pistol.shoot()  # 2-й выстрел
loaded_pistol.shoot()  # 3-й выстрел
loaded_pistol.shoot()  # Пусто!