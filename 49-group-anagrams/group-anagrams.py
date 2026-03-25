class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Словарь: ключ — отсортированная строка, значение — список анаграмм
        groups = {}
        
        # Проходим по каждой строке
        for s in strs:
            # Сортируем буквы, чтобы получить одинаковый ключ для анаграмм
            key = ''.join(sorted(s))
            
            # Если ключа нет в словаре, создаём новый список
            if key not in groups:
                groups[key] = []
            
            # Добавляем строку в соответствующую группу
            groups[key].append(s)
        
        # Возвращаем все группы
        return list(groups.values())