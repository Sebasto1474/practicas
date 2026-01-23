def dfs_n_queens(n):
    # Caso borde
    if n < 1:
        return []

    result = []

    def is_valid(state, row, col):
        """
        Verifica si se puede colocar una reina en (row, col)
        sin atacar a las reinas ya colocadas en state.
        """
        for prev_row in range(len(state)):
            prev_col = state[prev_row]

            # Misma columna
            if col == prev_col:
                return False

            # Misma diagonal
            if abs(col - prev_col) == abs(row - prev_row):
                return False

        return True

    def dfs(state):
        """
        DFS / Backtracking.
        state[i] = columna de la reina en la fila i
        """
        # Caso base: colocamos n reinas
        if len(state) == n:
            result.append(state)
            return

        # La fila actual está dada por la profundidad
        row = len(state)

        # Probar todas las columnas posibles en esta fila
        for col in range(n):
            if is_valid(state, row, col):
                dfs(state + [col])  # bajar un nivel

    # Comenzamos con un estado vacío
    dfs([])

    return result
