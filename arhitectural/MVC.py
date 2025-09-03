'''

MVC (Model-View-Controller) в Python — это архитектурный паттерн, который разделяет приложение на три компонента:
Модель (данные и бизнес-логика),
Представление (пользовательский интерфейс)
и Контроллер (обработка взаимодействия пользователя и данных).

Этот шаблон используется во многих Python-фреймворках для упрощения разработки и поддержки приложений,
позволяя независимо изменять каждый компонент.

    Модель
Отвечает за обработку данных и бизнес-логику приложения.
Она хранит всю информацию и методы, необходимые для выполнения основных функций.

    Представление
Это компонент, который отображает данные пользователю. Он отвечает за внешний вид приложения

    Контроллер
Обрабатывает взаимодействие пользователя с приложением.
Он принимает запросы от пользователя, управляет Моделью и выбирает подходящее
Представление для отображения результата.

'''


# модель - данные и бизнес-логика
class UserModel:
    def __init__(self):
        self.users = []

    def add_user(self, name):
        user = {"id": len(self.users) + 1, "name": name}
        self.users.append(user)
        return user

    def get_users(self):
        return self.users


# Представлекние - представление данных
class UserView:
    def show_users(self, users):
        print("Пользователи:")
        for user in users:
            print(f"  {user['id']}: {user['name']}")

    def get_name(self):
        return input("Введите имя: ")


# Контроллер - связывает модель и представление
class UserController:
    def __init__(self):
        self.model = UserModel()
        self.view = UserView()

    def add_user(self):
        name = self.view.get_name()
        self.model.add_user(name)
        print(f"Пользователь {name} добавлен")

    def show_all(self):
        users = self.model.get_users()
        self.view.show_users(users)



if __name__ == "__main__":
    controller = UserController()

    controller.add_user()
    controller.add_user()

    controller.show_all()