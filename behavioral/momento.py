# Снимок, простой обьект, который хранит внутреннее состояние Создателя
class Memento:
    def __init__(self, state: str):
        self._state = state

    def get_state(self) -> str:
        return self._state


# создатель, создает снимок вызывая save и восстанавливает вызывая restore, только создатель имеет доступк
# к состоянию хранящземуся в Снимке через метод get_state
class TextEditor:
    def __init__(self):
        self._text = ""

    def write(self, text: str):
        self._text += text

    def save(self) -> Memento:
        return Memento(self._text)

    def restore(self, memento: Memento):
        self._text = memento.get_state()

    def show(self):
        print(f"Текущий текст: '{self._text}'")


# опекун, управляет историей снимков, зарпашивает у создателя Новыый снимок history.backup(editor.save())
# хранит снимки self._mementos
# передает снимок обратно Создателю для восстановления editor.restore(history.undo())
# опекун никогда не работает с содержимым Снимка напрямую. Просто хранит и передает его
class History:
    def __init__(self):
        self._mementos = []

    def backup(self, memento: Memento):
        self._mementos.append(memento)

    def undo(self) -> Memento:
        return self._mementos.pop()


# Пример использования
if __name__ == "__main__":
    editor = TextEditor()
    history = History()

    editor.write("Привет")
    history.backup(editor.save())

    editor.show()

    editor.write(" мир")
    history.backup(editor.save())

    memento = history.undo()
    if memento:
        editor.restore(memento)
    editor.show()

    memento = history.undo()
    if memento:
        editor.restore(memento)
    editor.show()


''' 
Опекун просит Создателя сохранить состояние
Создатель создает Снимок и передает Опекуну
Опекун просто сохраняет Снимок в своем списке
Когда нужна отмена, Опекун достает последний Снимок и передает Создателю
Создатель использует Снимок чтобы восстановить свое состояние 
'''