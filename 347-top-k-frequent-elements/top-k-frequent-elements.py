class Solution:
    def topKFrequent(self, nums, k):
        # 1. Подсчёт частот
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # 2. Min-куча для k наиболее частых
        heap = []
        # Вспомогательные функции для кучи
        def bubble_up(i):
            while i > 0:
                parent = (i - 1) // 2
                if heap[i][0] < heap[parent][0]:  # сравниваем частоты
                    heap[i], heap[parent] = heap[parent], heap[i]
                    i = parent
                else:
                    break
        
        def bubble_down(i):
            n = len(heap)
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                smallest = i
                if left < n and heap[left][0] < heap[smallest][0]:
                    smallest = left
                if right < n and heap[right][0] < heap[smallest][0]:
                    smallest = right
                if smallest != i:
                    heap[i], heap[smallest] = heap[smallest], heap[i]
                    i = smallest
                else:
                    break
        
        def push(item):
            heap.append(item)
            bubble_up(len(heap) - 1)
        
        def pop():
            # удаляем корень (минимальный)
            if not heap:
                return None
            if len(heap) == 1:
                return heap.pop()
            root = heap[0]
            heap[0] = heap.pop()
            bubble_down(0)
            return root
        
        # Обрабатываем каждый элемент из словаря частот
        for num, cnt in freq.items():
            push((cnt, num))
            if len(heap) > k:
                pop()  # удаляем наименьшую частоту
        
        # Извлекаем числа из кучи
        result = []
        for cnt, num in heap:
            result.append(num)
        return result