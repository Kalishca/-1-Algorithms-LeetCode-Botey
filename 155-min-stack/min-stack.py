class MinStack:
    def __init__(self):
        # Основной стек для хранения всех элементов
        self.stack = []
        # Стек для хранения текущих минимумов
        self.min_stack = []

    def push(self, val: int) -> None:
        # Добавляем элемент в основной стек
        self.stack.append(val)
        # Если стек минимумов пуст или новый элемент меньше или равен текущему минимуму,
        # добавляем его в стек минимумов
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Удаляем элемент из основного стека
        if self.stack:
            val = self.stack.pop()
            # Если удаляемый элемент является текущим минимумом, удаляем его из стека минимумов
            if self.min_stack and val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        # Возвращаем верхний элемент основного стека
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        # Возвращаем текущий минимум (вершина стека минимумов)
        return self.min_stack[-1] if self.min_stack else None