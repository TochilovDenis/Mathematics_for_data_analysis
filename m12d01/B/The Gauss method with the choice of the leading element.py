def gauss_max_pivot(A, b):
    n = len(A)
    
    for k in range(n):
        # Поиск строки с максимальным элементом в текущем столбце
        max_index = k
        max_value = abs(A[k][k])
        
        for i in range(k + 1, n):
            if abs(A[i][k]) > max_value:
                max_value = abs(A[i][k])
                max_index = i
        
        # Проверка на вырожденность
        if max_value < 1e-12:
            return None
        
        # Перестановка строк
        if max_index != k:
            A[k], A[max_index] = A[max_index], A[k]
            b[k], b[max_index] = b[max_index], b[k]
        
        # Прямой ход
        for i in range(k + 1, n):
            factor = A[i][k] / A[k][k]
            # Вычитаем из строки i строку k, умноженную на factor
            A[i][k] = 0  # Явно обнуляем
            for j in range(k + 1, n):
                A[i][j] -= factor * A[k][j]
            b[i] -= factor * b[k]
    
    # Обратная подстановка
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]
    
    return x

def main():
    with open("input.txt", "r") as f:
        n = int(f.readline().strip())
        A = [list(map(float, f.readline().strip().split())) for _ in range(n)]
        b = list(map(float, f.readline().strip().split()))
    
    result = gauss_max_pivot([row[:] for row in A], b[:])
    
    if result is None:
        print("NO_SINGLE_SOLUTION")
    else:
        # Округление: для положительных +0.5, для отрицательных -0.5
        rounded = []
        for val in result:
            if val >= 0:
                rounded.append(str(int(val + 0.5)))
            else:
                rounded.append(str(int(val - 0.5)))
        print(" ".join(rounded))

if __name__ == "__main__":
    main()