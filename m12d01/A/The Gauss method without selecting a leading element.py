def gauss_no_pivot(n, A, b):
    # Прямой ход
    for k in range(n):
        # Проверяем ведущий элемент
        if A[k][k] == 0:
            return "NO_SINGLE_SOLUTION"
        
        # Нормализуем строку k
        factor = A[k][k]
        for j in range(k, n):
            A[k][j] /= factor
        b[k] /= factor
        
        # Вычитаем строку k из строк ниже
        for i in range(k + 1, n):
            coeff = A[i][k]
            for j in range(k, n):
                A[i][j] -= coeff * A[k][j]
            b[i] -= coeff * b[k]
    
    # Обратный ход
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
    # от n-1 до 0 включительно 
    # for c in range(n):
        # i=n-c-1
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i]  = x[i]- A[i][j] * x[j]
    
    # Округляем до ближайшего целого
    x_rounded = [round(val) for val in x]
    return x_rounded


def main():
    with open("input.txt", encoding="UTF-8") as file_in:
            lines = file_in.readlines()
            m=int(lines[0])
            mtr1= []
            for i in range(m):
                mtr1.append(list(map(int, lines[i+1].split())))

            v_b=list(map(int, lines[m+1].split()))
 
            result = gauss_no_pivot(m,mtr1,v_b)
            if result == "NO_SINGLE_SOLUTION":
                print("NO_SINGLE_SOLUTION")
            else:
                print(" ".join(map(str, result)))

 
if __name__ == "__main__":
    main()