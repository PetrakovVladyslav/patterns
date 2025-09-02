
from abc import ABC, abstractmethod

# абстрактный базовый обработчик, метод set_next - ключевой для цепочки
class SupportHandler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

# handle для обработки - если текущий обработчик не справился - отправляет дальше

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

# Конкретные обработчики
class TechnicalSupport(SupportHandler):
    def handle(self, request):
        if request.type == "technical" and request.complexity <= 3:
            return f"Техподдержка решил проблему '{request.description}'"
        return super().handle(request)


class SpecialistSupport(SupportHandler):
    def handle(self, request):
        if request.type == "technical" and request.complexity <= 7:
            return f"Специалист решил проблему '{request.description}'"
        return super().handle(request)


class ManagerSupport(SupportHandler):
    def handle(self, request):
        if request.type == "billing" or request.complexity <= 10:
            return f"Менеджер обработал запрос '{request.description}'"
        return super().handle(request)


class Request:
    def __init__(self, description, request_type, complexity):
        self.description = description
        self.type = request_type
        self.complexity = complexity


tech_support = TechnicalSupport()
specialist = SpecialistSupport()
manager = ManagerSupport()

#строим цепочку вызовов метода
tech_support.set_next(specialist).set_next(manager)

requests = [
    Request("проблема 1", "technical", 2),
    Request("проблема 2", "technical", 8),
    Request("проблема 3", "billing", 5),
    Request("проблема 3", "technical", 15)
]

print("Обработка заявок ")
for req in requests:
    result = tech_support.handle(req)
    if result:
        print(f"{result}")
    else:
        print(f"Никто не смог обработать: '{req.description}'")
    print()
