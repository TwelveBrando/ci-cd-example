def adjacency_matrix_to_list(matrix):
    adjacency_list = {}
    for i in range(len(matrix)):
        adjacency_list[i] = []
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                adjacency_list[i].append(j)
    return adjacency_list


adjacency_matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]
graph = adjacency_matrix_to_list(adjacency_matrix)
print(graph)
