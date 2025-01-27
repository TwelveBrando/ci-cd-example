def is_connected(matrix):
    n = len(matrix)
    visited = [False] * n

    def dfs(v):
        visited[v] = True
        for i in range(n):
            if matrix[v][i] == 1 and not visited[i]:
                dfs(i)

    dfs(0)
    return all(visited)


adjacency_matrix = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]
print(is_connected(adjacency_matrix))
