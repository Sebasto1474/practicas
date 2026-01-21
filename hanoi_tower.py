def hanoi_solver(n):
    a = list(range(n, 0, -1))
    b = []
    c = []
    moves = []
    moves.append(f"{a} {b} {c}")
    def move(n, source, auxiliary, target):
        if n == 1:
            target.append(source.pop())
            moves.append(f"{a} {b} {c}")
        else:
            move(n-1, source, target, auxiliary)
            target.append(source.pop())
            moves.append(f"{a} {b} {c}")
            move(n-1, auxiliary, source, target)
    move(n, a, b, c)
    return "\n".join(moves)

print(hanoi_solver(3))