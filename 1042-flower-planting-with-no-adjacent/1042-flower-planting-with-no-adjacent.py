class Solution:
    def gardenNoAdj(self, n, paths):
        graph = [[] for _ in range(n)]

        for u, v in paths:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

        flowers = [0] * n

        for garden in range(n):
            used = set()

            for neighbor in graph[garden]:
                if flowers[neighbor] != 0:
                    used.add(flowers[neighbor])

            for flower in range(1, 5):
                if flower not in used:
                    flowers[garden] = flower
                    break

        return flowers