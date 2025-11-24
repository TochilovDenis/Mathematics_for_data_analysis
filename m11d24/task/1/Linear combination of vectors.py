def main():

    # Чтение входных данных
    with open('input.txt', 'r') as f:
        k = int(f.readline().strip())
        
        # Читаем коэффициенты λ
        coefficients = list(map(float, f.readline().strip().split()))
        
        # Читаем векторы
        vectors = []
        for _ in range(k):
            vector = list(map(float, f.readline().strip().split()))
            vectors.append(vector)

        # Определяем размерность векторов
        n = len(vectors[0])

        # Инициализируем результирующий вектор нулями
        result = [0.0] * n

        # Вычисляем линейную комбинацию
        for i in range(k):
            for j in range(n):
                result[j] += coefficients[i] * vectors[i][j]

        # Форматируем вывод с точностью до 2 знаков после запятой
        formatted_result = [f'{x:.2f}' for x in result]

        # Выводим результат
        print(' '.join(formatted_result))


if __name__ == "__main__":
    main()
