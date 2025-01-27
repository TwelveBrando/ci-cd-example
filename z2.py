def incidence_matrizx_to_edges(matrix):
    edges = []
    for j in range(len(matrix[0])):
        start = None
        end = None
        for i in range(len(matrix)):
            if matrix[i][j] == 1:
                start = i
            elif matrix[i][j] == -1:
                end = i
        if start is not None and end is not None:
            edges.append((start, end))
    return edges


incidence_matrix = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [-1, 0, 0, 1],
    [0, -1, -1, 0]
]
edges = incidence_matrizx_to_edges(incidence_matrix)
print(edges)
