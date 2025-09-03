'''
MVP (Model-View-Presenter) – это архитектурный паттерн, который разделяет приложение на три компонента:
Model (данные и бизнес-логика),
View (пользовательский интерфейс)
Presenter (посредник между Model и View, обрабатывающий бизнес-логику).
В Python MVP используется для создания более поддерживаемого и тестируемого кода,
 изолируя логику представления от логики данных и облегчая их модульное тестирование

Model (Модель):
Содержит данные и бизнес-логику приложения, не зависит от представления

View (Представление):
Отвечает за отображение данных пользователю (UI) и обработку пользовательского ввода. В отличие от MVC, View не связан напрямую с Model.

Presenter (Презентатор):
Служит мостом между Model и View, получает данные из Model, обрабатывает их и передает View для отображения

В MVC:
Controller управляет потоком
View может напрямую обращаться к Model

В MVP:
View полностью пассивный - только отображает данные
Presenter содержит всю логику представления
View знает о Presenter (двусторонняя связь)
Model не знает ни о чём

'''


# модель  - валидация
class UserModel:
    def save_user(self, name, email):
        return "@" in email


# представление
class FormView:
    def __init__(self, presenter):
        self.presenter = presenter

    def show_message(self, message):
        print(message)

# События передаем презентатору
    def submit_form(self, name, email):
        self.presenter.handle_submit(name, email)


# презентатор - обрабатывает события
class FormPresenter:
    def __init__(self):
        self.model = UserModel()
        self.view = FormView(self)

    def handle_submit(self, name, email):
        if self.model.save_user(name, email):
            self.view.show_message("Успех")
        else:
            self.view.show_message("Ошибка")


presenter = FormPresenter()
presenter.view.submit_form("Vladyslav", "vladyslav@mail.com")