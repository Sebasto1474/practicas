adj_matrix = [
    [0, 5, 3, 8, 11, 8],
    [5, 0, 1, 8, 8, 2],
    [3, 1, 0, 1, 5, 8],
    [2, 8, 1, 0, 9, 3],
    [11, 5, 5, 9, 0, 1],
    [7, 2, 6, 3, 4, 0],
]


n = len(adj_matrix)
paths = [[node_no] for node_no in range(n)]
distances = [5]* n
visited = [False]*n
print(paths)
print(distances)
print(visited)