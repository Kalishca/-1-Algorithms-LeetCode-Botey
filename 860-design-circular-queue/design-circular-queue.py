class MyCircularQueue:
    def __init__(self, k: int):
        """
        Инициализация очереди фиксированного размера k.
        Используются:
        - queue: список длины k для хранения элементов
        - head: индекс первого элемента (головы)
        - tail: индекс следующей свободной позиции (куда будет добавлен новый элемент)
        - count: текущее количество элементов в очереди
        """
        self.queue = [0] * k
        self.head = 0
        self.tail = 0
        self.count = 0
        self.size = k

    def enQueue(self, value: int) -> bool:
        """Добавляет элемент в конец очереди. Возвращает True при успехе, иначе False."""
        if self.isFull():
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.size
        self.count += 1
        return True

    def deQueue(self) -> bool:
        """Удаляет элемент из начала очереди. Возвращает True при успехе, иначе False."""
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return True

    def Front(self) -> int:
        """Возвращает первый элемент очереди или -1, если очередь пуста."""
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        """Возвращает последний элемент очереди или -1, если очередь пуста."""
        if self.isEmpty():
            return -1
        # Последний элемент находится по индексу (tail - 1) с учётом циклического оборачивания
        last_index = (self.tail - 1) % self.size
        return self.queue[last_index]

    def isEmpty(self) -> bool:
        """Проверяет, пуста ли очередь."""
        return self.count == 0

    def isFull(self) -> bool:
        """Проверяет, заполнена ли очередь."""
        return self.count == self.size
