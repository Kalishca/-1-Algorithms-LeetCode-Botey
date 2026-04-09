from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # 1. Набор кандидатов: все рёбра (вес, u, v)
        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                edges.append((abs(x1 - x2) + abs(y1 - y2), i, j))
        
        # 2. Жадный выбор: сортируем по весу (целевая функция - минимизация суммы)
        edges.sort()
        
        # DSU (система непересекающихся множеств) без отдельного класса
        parent = list(range(n))
        rank = [0] * n
        
        def find(x):
            # Сжатие пути
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            # Объединение по рангу
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1
            return True
        
        total = 0
        cnt = 0
        # 3. Перебираем рёбра в порядке возрастания веса
        for w, u, v in edges:
            if union(u, v):          # безопасное ребро (не создаёт цикл)
                total += w
                cnt += 1
                if cnt == n - 1:     # остовное дерево готово
                    break
        
        return total