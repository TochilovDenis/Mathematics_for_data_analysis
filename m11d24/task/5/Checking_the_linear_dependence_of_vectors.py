def are_vectors_linearly_dependent(vectors, m, n):
    """Проверяет линейную зависимость векторов методом Гаусса"""
    # Создаем матрицу для преобразований
    mat = [row[:] for row in vectors]
    
    # Приводим матрицу к ступенчатому виду
    for col in range(min(m, n)):
        # Ищем ненулевой элемент в текущем столбце
        pivot_row = col
        while pivot_row < m and abs(mat[pivot_row][col]) < 1e-10:
            pivot_row += 1
        
        if pivot_row == m:
            continue  # Все нули в столбце
        
        # Меняем строки местами
        if pivot_row != col:
            mat[col], mat[pivot_row] = mat[pivot_row], mat[col]
        
        # Обнуляем элементы ниже ведущего
        for i in range(col + 1, m):
            factor = mat[i][col] / mat[col][col]
            for j in range(col, n):
                mat[i][j] -= factor * mat[col][j]
    
    # Подсчитываем ненулевые строки (ранг)
    rank = 0
    for i in range(m):
        if any(abs(x) > 1e-10 for x in mat[i]):
            rank += 1
    
    return rank < m


def main():
    with open('input.txt', 'r') as f:
        m, n = map(int, f.readline().split())
        vectors = []
        
        for _ in range(m):
            vector = list(map(float, f.readline().split()))
            vectors.append(vector)
    
    if are_vectors_linearly_dependent(vectors, m, n):
        print("LINEARLY_DEPENDENT")
    else:
        print("LINEARLY_INDEPENDENT")


if __name__ == "__main__":
    main()