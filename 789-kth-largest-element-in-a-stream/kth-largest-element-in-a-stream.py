class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = []
        for val in nums:
            self.add(val)

    def add(self, val):
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)
        if len(self.heap) > self.k:
            self._pop_min()
        return self.heap[0]

    def _bubble_up(self, i):
        while i > 0 and self.heap[i] < self.heap[(i - 1) // 2]:
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2

    def _bubble_down(self, i):
        n = len(self.heap)
        while True:
            left, right, smallest = 2 * i + 1, 2 * i + 2, i
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == i:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

    def _pop_min(self):
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if self.heap:
            self._bubble_down(0)