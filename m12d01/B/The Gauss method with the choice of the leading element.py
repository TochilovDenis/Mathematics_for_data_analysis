def gauss_with_pivot(n, A, b):
    # Прямой ход
    for k in range(n):
        # Находим строку с максимальным по модулю элементом в столбце k
        max_row = k
        max_val = abs(A[max_row][k])
        for i in range(k + 1, n):
            if abs(A[i][k]) > max_val:
                max_row = i
                max_val = abs(A[i][k])
        
        # Проверяем, что максимальный элемент не равен нулю
        if max_val == 0:
            return "NO_SINGLE_SOLUTION"
        
        # Переставляем строки
        if max_row != k:
            A[k], A[max_row] = A[max_row], A[k] 
            b[k], b[max_row] = b[max_row], b[k]
        
        # Прямое исключение
        for i in range(k + 1, n):
            factor = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= factor * A[k][j]
            b[i] -= factor * b[k]
    
    # Проверяем последний диагональный элемент
    if A[n-1][n-1] == 0:
        return "NO_SINGLE_SOLUTION"
    
    # Обратный ход
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        sum_ax = 0.0
        for j in range(i + 1, n):
            sum_ax += A[i][j] * x[j]
        x[i] = (b[i] - sum_ax) / A[i][i]
    
    # Округляем до ближайшего целого
    x_rounded = [round(val) for val in x]
    return x_rounded


def main():
    with open("input.txt", encoding="UTF-8") as file_in:
        lines = file_in.readlines()
        n = int(lines[0])
        A = []
        for i in range(n):
            A.append(list(map(int, lines[i+1].split())))
        
        b = list(map(int, lines[n+1].split()))
        
        result = gauss_with_pivot(n, A, b)
        if result == "NO_SINGLE_SOLUTION":
            print("NO_SINGLE_SOLUTION")
        else:
            print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()