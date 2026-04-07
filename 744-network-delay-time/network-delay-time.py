class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Возвращает минимальное время, за которое сигнал из узла k достигнет всех узлов.
        Используется алгоритм Дейкстры с простой реализацией (без кучи) за O(n^2).
        """
        # Построение списка смежности (индексы вершин от 0 до n-1)
        graph = [[] for _ in range(n)]
        for u, v, w in times:
            graph[u-1].append((v-1, w))

        INF = 10**9
        dist = [INF] * n
        dist[k-1] = 0
        visited = [False] * n

        for _ in range(n):
            # Находим непосещённую вершину с минимальным расстоянием
            u = -1
            min_dist = INF
            for i in range(n):
                if not visited[i] and dist[i] < min_dist:
                    min_dist = dist[i]
                    u = i
            if u == -1:  # нет достижимых вершин
                break
            visited[u] = True

            # Релаксация всех рёбер из u
            for v, w in graph[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w

        # Ищем максимальное расстояние среди всех вершин
        max_dist = max(dist)
        return -1 if max_dist == INF else max_dist