class OldGamepad:
    def press_a(self):
        return "Старый геймпад: A нажата"

    def press_b(self):
        return "Старый геймпад: B нажата"

class ModernController:
    def action(self):
        return "Современный контроллер: Действие"

    def jump(self):
        return "Современный контроллер: Прыжок"

class GamepadAdapter:
    def __init__(self, old_gamepad):
        self.old_gamepad = old_gamepad

    def action(self):
        return self.old_gamepad.press_a()

    def jump(self):
        return self.old_gamepad.press_b()

class Game:
    def play(self, controller):
        print(controller.action())
        print(controller.jump())

game = Game()

modern = ModernController()
print("Современный контроллер")
game.play(modern)

print()

old_gamepad = OldGamepad()
adapter = GamepadAdapter(old_gamepad)
print("Старый геймпад через адаптер")
game.play(adapter)