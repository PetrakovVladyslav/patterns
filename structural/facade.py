class GraphicsEngine:
    def load_textures(self):
        print("Загрузка текстур...")

    def init_renderer(self):
        print("Инициализация рендера...")

class AudioEngine:
    def load_sounds(self):
        print("Загрузка звуков...")

    def set_volume(self, volume):
        print(f"Громкость: {volume}%")


class InputManager:
    def init_keyboard(self):
        print("Инициализация клавиатуры...")

    def init_mouse(self):
        print("Инициализация мыши...")


class NetworkManager:
    def connect_server(self):
        print("Подключение к серверу...")

class SaveSystem:
    def load_save_file(self):
        print("Загрузка сохранения...")

class GameEngine:
    def __init__(self):
        self.graphics = GraphicsEngine()
        self.audio = AudioEngine()
        self.input = InputManager()
        self.network = NetworkManager()
        self.save = SaveSystem()

    def start_game(self):

        print("ЗАПУСК ИГРЫ ")
        self.graphics.load_textures()
        self.graphics.init_renderer()
        self.audio.load_sounds()
        self.audio.set_volume(80)
        self.input.init_keyboard()
        self.input.init_mouse()
        self.save.load_save_file()
        print("Игра готова!\n")

    def start_multiplayer(self):

        print("МУЛЬТИПЛЕЕР")
        self.network.connect_server()
        self.graphics.init_renderer()
        self.audio.set_volume(60)
        self.input.init_keyboard()
        print("Мультиплеер готов!\n")

game = GameEngine()

print("Запуск одиночной игры:")
game.start_game()

print("Запуск мультиплеера:")
game.start_multiplayer()