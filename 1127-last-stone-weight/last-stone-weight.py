class Solution(object):
    def lastStoneWeight(self, stones):
        # Строим max-кучу из камней
        heap = stones[:]  # копируем, чтобы не изменять исходный массив
        n = len(heap)

        # Просеивание вниз (для max-кучи)
        def heapify_down(i, size):
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                largest = i
                if left < size and heap[left] > heap[largest]:
                    largest = left
                if right < size and heap[right] > heap[largest]:
                    largest = right
                if largest != i:
                    heap[i], heap[largest] = heap[largest], heap[i]
                    i = largest
                else:
                    break

        # Просеивание вверх
        def heapify_up(i):
            while i > 0:
                parent = (i - 1) // 2
                if heap[i] > heap[parent]:
                    heap[i], heap[parent] = heap[parent], heap[i]
                    i = parent
                else:
                    break

        # Построение кучи за O(n)
        for i in range(n // 2 - 1, -1, -1):
            heapify_down(i, n)

        size = n
        while size > 1:
            # Извлекаем первый максимум (корень)
            first = heap[0]
            heap[0] = heap[size - 1]
            size -= 1
            heapify_down(0, size)

            # Извлекаем второй максимум
            second = heap[0]
            heap[0] = heap[size - 1]
            size -= 1
            heapify_down(0, size)

            if first != second:
                # Разница возвращается в кучу
                diff = first - second  # так как first >= second
                heap[size] = diff
                size += 1
                heapify_up(size - 1)

        # Если камней не осталось, возвращаем 0
        return heap[0] if size == 1 else 0