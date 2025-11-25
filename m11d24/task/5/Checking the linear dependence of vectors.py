import numpy as np


def main():
    with open('input.txt', 'r') as f:
        
        m, n = map(int, f.readline().strip().split())
        v = []

        for _ in range(m):
            v1 = list(map(float, f.readline().split()))
            v.append(v1)

        # Преобразуем в массив numpy
        matrix = np.array(v)
        # Вычисляем ранг матрицы
        r = np.linalg.matrix_rank(matrix)
        
        if r < m:
            print("LINEARLY_DEPENDENT")
        else:
            print("LINEARLY_INDEPENDENT")


if __name__ == "__main__":
    main()
