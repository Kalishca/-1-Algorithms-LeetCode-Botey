class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Создаём пустое множество для хранения уникальных элементов
        seen = set()
        
        # Проходим по каждому элементу массива
        for num in nums:
            # Если элемент уже есть во множестве, найден дубликат
            if num in seen:
                return True
            # Иначе добавляем элемент во множество
            seen.add(num)
        
        # Если дубликат не найден, возвращаем False
        return False     