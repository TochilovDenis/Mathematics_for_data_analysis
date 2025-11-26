import numpy as np

def main():
    with open('input.txt', 'r') as f:
        v1 = np.array(list(map(int, f.readline().strip().split())))
        v2 = np.array(list(map(int, f.readline().strip().split())))
        v3 = np.array(list(map(int, f.readline().strip().split())))
    
    result_lambda1 = -11
    result_lambda2 = -11
    
    for lambda1 in range(-10, 11):
        for lambda2 in range(-10, 11):
            # Вычисляем линейную комбинацию с помощью NumPy
            mas = lambda1 * v1 + lambda2 * v2
            
            # Сравниваем массивы с использованием np.array_equal
            if np.array_equal(mas, v3):
                result_lambda1 = lambda1
                result_lambda2 = lambda2
                break
        
        if result_lambda1 != -11:
            break
    
    if result_lambda1 != -11:
        print(f"{result_lambda1} {result_lambda2}")
    else:
        print("NO_SOLUTION")

if __name__ == "__main__":
    main()