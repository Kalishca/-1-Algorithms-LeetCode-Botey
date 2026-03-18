
class MyQueue:
    def __init__(self):
        # Инициализация двух стеков
        self.stack_in = []   # стек для добавления элементов (вход)
        self.stack_out = []  # стек для извлечения элементов (выход)

    def push(self, x: int) -> None:
        # Помещаем элемент в стек входа
        self.stack_in.append(x)

    def pop(self) -> int:
        # Если стек выхода пуст, перекладываем все элементы из стека входа
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        # Извлекаем верхний элемент из стека выхода (он соответствует первому добавленному)
        return self.stack_out.pop()

    def peek(self) -> int:
        # Аналогично pop, но без удаления
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def empty(self) -> bool:
        # Очередь пуста, если оба стека пусты
        return not self.stack_in and not self.stack_out