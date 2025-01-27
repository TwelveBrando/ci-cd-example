import numpy as np


def adjacency_matrix_to_edges(adj_matrix):
    edges = []
    n = len(adj_matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if adj_matrix[i][j] == 1:
                edges.append((i, j))
    return edges


def incidence_matrix_to_edges(inc_matrix):
    edges = []
    n, m = inc_matrix.shape
    for j in range(m):
        start = None
        end = None
        for i in range(n):
            if inc_matrix[i][j] == 1:
                if start is None:
                    start = i
                else:
                    end = i
        if start is not None and end is not None:
            edges.append((start, end))
    return edges


adj_matrix = np.array([[0, 1, 1],
                      [1, 0, 1],
                      [1, 1, 0]])
inc_matrix = np.array([[1, 0, 1],
                       [1, 1, 0],
                       [0, 1, 1]])
edges_from_adj = adjacency_matrix_to_edges(adj_matrix)
edges_from_inc = incidence_matrix_to_edges(inc_matrix)
print("Рёбра из матрицы смежности:", edges_from_adj)
print("Рёбра из матрицы инцидентности:", edges_from_inc)
