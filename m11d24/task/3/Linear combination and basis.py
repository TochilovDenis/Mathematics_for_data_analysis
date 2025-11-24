def main():
    with open('input.txt', 'r') as f:
        v1 = list(map(int, f.readline().strip().split()))
        v2 = list(map(int, f.readline().strip().split()))
        v3 = list(map(int, f.readline().strip().split()))
    
    n = len(v1)
    
    # Инициализируем коэффициенты значениями, которые заведомо не в диапазоне
    result_lambda1 = -11
    result_lambda2 = -11
    
    for lambda1 in range(-10, 11):
        for lambda2 in range(-10, 11):
            mas = [0] * n
            
            vectors = [v1, v2]
            lambdas = [lambda1, lambda2]
            
            for i in range(2):
                current_vector = vectors[i]
                current_lambda = lambdas[i]
                for y in range(n):
                    mas[y] += current_vector[y] * current_lambda
            
            if mas == v3:
                result_lambda1 = lambda1
                result_lambda2 = lambda2
                break
        
        # Проверяем, нашли ли решение во внутреннем цикле
        if result_lambda1 != -11:
            break
    
    if result_lambda1 != -11:
        print(f"{result_lambda1} {result_lambda2}")
    else:
        print("NO_SOLUTION")

if __name__ == "__main__":
    main()