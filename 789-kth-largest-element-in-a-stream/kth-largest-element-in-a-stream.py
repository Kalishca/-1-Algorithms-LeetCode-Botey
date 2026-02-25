class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = []  # min-heap для хранения k наибольших элементов
        for val in nums:
            self.add(val)

    def add(self, val):
        # Вставка нового элемента
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)
        # Если размер превысил k, удаляем минимальный
        if len(self.heap) > self.k:
            self._pop_min()
        return self.heap[0]

    def _bubble_up(self, i):
        """Поднимает элемент вверх, пока он меньше родителя"""
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def _bubble_down(self, i):
        """Опускает элемент вниз, пока он больше одного из детей"""
        n = len(self.heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest != i:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
            else:
                break

    def _pop_min(self):
        """Удаляет корень (минимальный элемент) и восстанавливает кучу"""
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if self.heap:
            self._bubble_down(0)