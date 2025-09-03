'''

MVVM (Model-View-ViewModel) —  разделяет приложение на три основных компонента:
Model (бизнес-логика и данные),
View (пользовательский интерфейс) и
ViewModel (посредник между Model и View),
обеспечивая слабую связь между ними и упрощая разработку, тестирование и поддержку приложения.

    Model (Модель): Отвечает за данные и бизнес-логику приложения.
Не знает о существовании View или ViewModel.

    View (Представление):Пользовательский интерфейс приложения.
Отображает данные, полученные от ViewModel.
Отправляет действия пользователя (нажатия кнопок, ввод текста) обратно в ViewModel.
Слабо связан с Model.

    ViewModel (Модель Представления):
    Посредник между Model и View.
Содержит логику представления, преобразует данные из Model в формат, пригодный для отображения в View.
Реагирует на действия пользователя из View, передавая их в Model для обработки, и обновляет View при изменении данных в Model.
Не имеет прямого доступа к View.

'''

#Model
class CounterModel:
# хранит данные _count
    def __init__(self):
        self._count = 0

    def increment(self):
        self._count += 1

    def get_count(self):
        return self._count


#ViewModel
class CounterViewModel:
# обращается к Модели чтобы получить данные
    def __init__(self, model):
        self.model = model
        self.count_text = f"Текущее значение: {self.model.get_count()}"

    def increment_command(self):
        self.model.increment()
        self.count_text = f"Текущее значение: {self.model.get_count()}"


#View - отображает тексти передает действия обратно в ViewModelk
class ConsoleView:
    def __init__(self, view_model):
        self.vm = view_model

    def render(self):
        print(self.vm.count_text)

    def user_action(self):
        command = input("Нажмите Enter, чтобы увеличить счётчик, или q для выхода: ")
        if command == "":
            self.vm.increment_command()
            return True
        return False


if __name__ == "__main__":
    model = CounterModel()
    vm = CounterViewModel(model)
    view = ConsoleView(vm)

    while True:
        view.render()
        if not view.user_action():
            break