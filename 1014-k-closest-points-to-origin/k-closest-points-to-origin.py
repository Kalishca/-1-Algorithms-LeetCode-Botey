class Solution(object):
    def kClosest(self, points, k):
        # Макс-куча размера k, хранит пары (квадрат расстояния, точка)
        heap = []
        for point in points:
            x, y = point
            dist = x*x + y*y
            if len(heap) < k:
                # Добавляем точку в кучу и восстанавливаем порядок снизу вверх
                heap.append((dist, point))
                self._bubble_up(heap, len(heap)-1)
            else:
                # Если текущее расстояние меньше максимального в куче (корня)
                if dist < heap[0][0]:
                    # Заменяем корень и восстанавливаем порядок сверху вниз
                    heap[0] = (dist, point)
                    self._bubble_down(heap, 0)
        # Возвращаем только точки (без расстояний)
        return [point for _, point in heap]

    def _bubble_up(self, heap, i):
        """Поднимает элемент вверх, пока он больше родителя (max-heap)"""
        while i > 0:
            parent = (i - 1) // 2
            if heap[i][0] > heap[parent][0]:
                heap[i], heap[parent] = heap[parent], heap[i]
                i = parent
            else:
                break

    def _bubble_down(self, heap, i):
        """Опускает элемент вниз, пока он меньше одного из детей"""
        n = len(heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i
            if left < n and heap[left][0] > heap[largest][0]:
                largest = left
            if right < n and heap[right][0] > heap[largest][0]:
                largest = right
            if largest != i:
                heap[i], heap[largest] = heap[largest], heap[i]
                i = largest
            else:
                break