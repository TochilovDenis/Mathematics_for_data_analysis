import numpy as np

def check_matrix_type_numpy(n, matrix):
    # Преобразуем в numpy array
    A = np.array(matrix)
    
    # Создаем маски для разных областей матрицы
    i, j = np.indices(A.shape)
    
    # Проверка диагональной: все вне диагонали == 0
    is_diagonal = np.all(A[i != j] == 0)
    
    # Проверка верхнетреугольной: все ниже диагонали == 0
    is_upper = np.all(A[i > j] == 0)
    
    # Проверка нижнетреугольной: все выше диагонали == 0
    is_lower = np.all(A[i < j] == 0)
    
    if is_diagonal:
        return "DIAGONAL"
    elif is_upper:
        return "UPPER_TRIANGULAR"
    elif is_lower:
        return "LOWER_TRIANGULAR"
    else:
        return "OTHER"

def main():
    # Чтение входных данных из файла
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())
        matrix = []
        for _ in range(n):
            row = list(map(float, f.readline().split()))
            matrix.append(row)
    
    # Проверка типа матрицы с использованием NumPy
    result = check_matrix_type_numpy(n, matrix)
    print(result)

if __name__ == "__main__":
    main()