from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """
        Возвращает количество столбцов, которые не являются лексикографически
        отсортированными (по неубыванию) сверху вниз.
        """
        # Если массив пуст или строки отсутствуют, удалять нечего
        if not strs:
            return 0

        rows = len(strs)          # количество строк
        cols = len(strs[0])       # количество столбцов (все строки одной длины)
        delete_count = 0

        # Перебираем каждый столбец
        for c in range(cols):
            # Проверяем, отсортирован ли столбец по неубыванию
            for r in range(1, rows):
                if strs[r][c] < strs[r-1][c]:
                    # Нарушение порядка: текущий символ меньше предыдущего
                    delete_count += 1
                    break  # переходим к следующему столбцу

        return delete_count