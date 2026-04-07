from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        if original == color:
            return image

        rows, cols = len(image), len(image[0])

        # Самодельная очередь на списке
        queue = [None] * (rows * cols)
        head = 0
        tail = 0

        # Помещаем стартовую вершину в очередь и сразу меняем её цвет (становится "серой")
        queue[tail] = (sr, sc)
        tail += 1
        image[sr][sc] = color

        while head < tail:
            # Извлекаем вершину из очереди (аналог u = EXTRACT-MIN)
            r, c = queue[head]
            head += 1

            # Перебираем всех соседей (рёбра графа)
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original:
                    # Обнаружили новую вершину того же цвета – добавляем в очередь
                    queue[tail] = (nr, nc)
                    tail += 1
                    # Меняем цвет сразу (вершина становится "серой") – как в лекции при первом обнаружении
                    image[nr][nc] = color

        return image