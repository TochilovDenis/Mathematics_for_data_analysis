import math

def main():
    # Чтение матрицы из файла
    with open("input.txt", 'r') as file:
        m, n = map(int, file.readline().split())
        matrix = []
        for _ in range(m):
            row = list(map(float, file.readline().split()))
            matrix.append(row)
    
    # Нормализация матрицы по столбцам
    normalized = [[0 for _ in range(n)] for _ in range(m)]
    
    for j in range(n):  # для каждого столбца
        # Вычисляем среднее значение столбца
        column_sum = 0
        for i in range(m):
            column_sum += matrix[i][j]
        mean = column_sum / m
        
        # Вычисляем стандартное отклонение столбца
        variance_sum = 0
        for i in range(m):
            variance_sum += (matrix[i][j] - mean) ** 2
        std_dev = math.sqrt(variance_sum / m)
        
        # Нормализуем элементы столбца
        for i in range(m):
            if std_dev == 0:  # избегаем деления на ноль
                normalized_value = 0
            else:
                normalized_value = (matrix[i][j] - mean) / std_dev
            # Отбрасываем дробную часть (приводим к int)
            normalized[i][j] = int(normalized_value)
    
    # Вывод результата
    for row in normalized:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()