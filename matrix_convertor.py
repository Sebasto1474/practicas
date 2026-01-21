new_adj_list = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [2]
}

def adjacency_list_to_matrix(adj_list):
    n = len(adj_list)
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for nodes, neighbors in adj_list.items():
        for neighbor in neighbors:
            matrix[nodes][neighbor] = 1

    for row in matrix:
        print(row)
    return matrix