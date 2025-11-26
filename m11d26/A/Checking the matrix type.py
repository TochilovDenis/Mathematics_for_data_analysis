def main():
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())
        matrix = []
        for _ in range(n):
            row = list(map(float, f.readline().split()))
            matrix.append(row)

        is_diagonal = True
        is_upper = True
        is_lower = True
        
        for i in range(n):
            for j in range(n):
                # Проверка для диагональной матрицы
                if i != j and matrix[i][j] != 0:
                    is_diagonal = False
                
                # Проверка для верхнетреугольной матрицы
                if i > j and matrix[i][j] != 0:
                    is_upper = False
                
                # Проверка для нижнетреугольной матрицы
                if i < j and matrix[i][j] != 0:
                    is_lower = False
        
        # Определяем приоритет: диагональная > верхнетреугольная/нижнетреугольная
        if is_diagonal:
            print("DIAGONAL")
        elif is_upper:
            print("UPPER_TRIANGULAR")
        elif is_lower:
            print("LOWER_TRIANGULAR")
        else:
            print("OTHER")
        

if __name__ == "__main__":
    main()