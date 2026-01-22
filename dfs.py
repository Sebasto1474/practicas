def dfs(matrix, start_node):
    n = len(matrix)
    stack = [start_node]
    visited = [False]*n
    result = []
    while stack:
        current = stack.pop()
        if visited[current]:
            continue
        else:
            visited[current] = True
            result.append(current)