class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Создаём множество для хранения уникальных элементов первого массива
        set1 = set(nums1)
        
        # Создаём множество для хранения результата (автоматически исключает дубликаты)
        result = set()
        
        # Проходим по второму массиву
        for num in nums2:
            # Если элемент присутствует в первом множестве, добавляем его в результат
            if num in set1:
                result.add(num)
        
        # Преобразуем множество в список и возвращаем
        return list(result)        