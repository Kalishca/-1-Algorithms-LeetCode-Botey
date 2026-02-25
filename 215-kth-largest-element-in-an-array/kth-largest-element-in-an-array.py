class Solution(object):
    def findKthLargest(self, nums, k):

        def max_heapify(A, i, heap_size):
            l = 2 * i
            r = 2 * i + 1
            largest = i

            if l <= heap_size and A[l] > A[largest]:
                largest = l

            if r <= heap_size and A[r] > A[largest]:
                largest = r

            if largest != i:
                A[i], A[largest] = A[largest], A[i]
                max_heapify(A, largest, heap_size)

        n = len(nums)
        A = [0] + nums  # делаем 1-индексацию
        heap_size = n

        # build heap
        for i in range(n // 2, 0, -1):
            max_heapify(A, i, heap_size)

        # извлекаем максимум k-1 раз
        for _ in range(k - 1):
            A[1], A[heap_size] = A[heap_size], A[1]
            heap_size -= 1
            max_heapify(A, 1, heap_size)

        return A[1]