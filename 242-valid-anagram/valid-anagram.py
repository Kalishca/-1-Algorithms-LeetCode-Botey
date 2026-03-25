class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Если длины строк не равны, они не могут быть анаграммами
        if len(s) != len(t):
            return False
        
        # Создаём словарь для подсчёта частоты символов
        count = {}
        
        # Подсчитываем частоту символов в строке s
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # Проверяем строку t, уменьшая счётчики
        for char in t:
            # Если символа нет в словаре или его счётчик стал отрицательным
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        
        # Если все проверки пройдены, строки являются анаграммами
        return True