class GunInterface:
    def shoot(self):
        raise NotImplementedError

class Gun(GunInterface):
    def shoot(self):
        print("Выстрел!")

class AmmoProxy(GunInterface):
    def __init__(self, gun, ammo):
        self._gun = gun
        self._ammo = ammo

    def shoot(self):
        if self._ammo > 0:
            self._ammo -= 1
            self._gun.shoot()
            print(f"Патронов осталось: {self._ammo}")
        else:
            print("Нет патронов!")

    def reload(self, ammo):
        self._ammo += ammo
        print(f"Патроны пополнены. Сейчас {self._ammo} патронов.")


pistol = Gun()
proxy = AmmoProxy(pistol, ammo=3)

proxy.shoot()
proxy.shoot()
proxy.reload(2)
proxy.shoot()
