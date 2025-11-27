def read_matrix(file_path):
    with open(file_path, 'r') as file:
        # Чтение размеров матрицы
        m, n = map(int, file.readline().split())
        
        # Чтение матрицы A
        A = []
        for _ in range(m):
            row = list(map(int, file.readline().split()))
            A.append(row)
    
    return A, m, n

def transpose_matrix(A, m, n):
    """Транспонирование матрицы A размером m x n"""
    # Создаем матрицу At размером n x m
    At = [[0 for _ in range(m)] for _ in range(n)]
    
    # Заполняем транспонированную матрицу
    for i in range(m):      # строки исходной матрицы
        for j in range(n):  # столбцы исходной матрицы
            At[j][i] = A[i][j]
    
    return At

def print_matrix(matrix):
    """Вывод матрицы"""
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    # Чтение входных данных
    A, m, n = read_matrix("input.txt")
    
    # Транспонирование матрицы
    At = transpose_matrix(A, m, n)
    
    # Вывод результата
    print_matrix(At)

if __name__ == "__main__":
    main()