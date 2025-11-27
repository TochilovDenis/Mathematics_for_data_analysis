def read_matrix(file_path):
    with open(file_path, 'r') as file:
        n = int(file.readline())
        matrix = []
        for _ in range(n):
            row = list(map(int, file.readline().split()))
            matrix.append(row)
    return matrix, n


def is_zero_matrix(matrix, n):
    """Проверяет, является ли матрица нулевой"""
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                return False
    return True


def matrix_multiply(A, B, n):
    """Умножение двух матриц размера n x n"""
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for l in range(n):
                result[i][j] += A[i][l] * B[l][j]
    return result

def find_nilpotent_degree(matrix, n):
    """Находит наименьшее k, такое что A^k = 0"""
    # Проверяем A^1
    if is_zero_matrix(matrix, n):
        return 1
    # Начинаем с A^1
    current_power = matrix
    k = 1
    # Так как k ≤ 100, ограничиваем цикл
    while k <= 100:
        k += 1
        # Вычисляем A^k = A^(k-1) * A
        current_power = matrix_multiply(current_power, matrix, n)
        if is_zero_matrix(current_power, n):
            return k
    return k  # В теории не должно сюда дойти по условию


def main():
    # Чтение входных данных
    A, n = read_matrix("input.txt")
    # Поиск степени нильпотентности
    k = find_nilpotent_degree(A, n)
    # Вывод результата
    print(k)


if __name__ == "__main__":
    main()