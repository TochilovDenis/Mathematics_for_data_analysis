def gauss_simple(A, b):
    n = len(A)
    
    for k in range(n):
        # Проверка с небольшой погрешностью
        if abs(A[k][k]) < 1e-9:
            return None
        
        # Прямой ход
        for i in range(k + 1, n):
            factor = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= factor * A[k][j]
            b[i] -= factor * b[k]
    
    # Обратная подстановка
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))) / A[i][i]
        
    return x


def main():
    with open("input.txt", "r") as f:
        n = int(f.readline())
        A = [list(map(float, f.readline().split())) for _ in range(n)]
        b = list(map(float, f.readline().split()))
    
    result = gauss_simple([row[:] for row in A], b[:])
    
    if result is None:
        print("NO_SINGLE_SOLUTION")
    else:
        print(" ".join(str(round(x)) for x in result))


if __name__ == "__main__":
    main()