from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Возвращает минимальное количество минут, через которое все апельсины станут гнилыми.
        Если это невозможно, возвращает -1.
        Используется многоисточниковый поиск в ширину (BFS) с ручной очередью.
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        # Ручная очередь для BFS (максимальный размер - все клетки)
        queue = [None] * (rows * cols)
        head = 0
        tail = 0

        fresh_count = 0

        # Первоначальный проход: считаем свежие апельсины и добавляем гнилые в очередь
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] == 2:
                    queue[tail] = (r, c)
                    tail += 1

        # Если свежих нет сразу, возвращаем 0
        if fresh_count == 0:
            return 0

        minutes = 0
        # Направления для соседей (вверх, вниз, влево, вправо)
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        # BFS: пока очередь не пуста и есть свежие апельсины
        while head < tail:
            # Чтобы отслеживать минуты, обрабатываем текущий уровень (все апельсины, добавленные на этой минуте)
            level_size = tail - head
            minutes += 1
            for _ in range(level_size):
                r, c = queue[head]
                head += 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        # Заражение свежего апельсина
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue[tail] = (nr, nc)
                        tail += 1
            # Если свежих не осталось, выходим (минуты уже увеличены на эту минуту)
            if fresh_count == 0:
                break

        return minutes if fresh_count == 0 else -1