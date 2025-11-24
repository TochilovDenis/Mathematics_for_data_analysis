def newton_method(a, b, c, x0, epsilon):
    """
    Метод Ньютона для нахождения корня квадратичной функции f(x) = ax^2 + bx + c
    """
    def f(x):
        return a * x * x + b * x + c
    
    def f_prime(x):
        return 2 * a * x + b
    
    x_current = x0
    iterations = 0
    max_iterations = 1000
    
    # Сначала проверяем, не является ли начальное приближение уже решением
    if abs(f(x_current)) < epsilon:
        return x_current, iterations
    
    while iterations < max_iterations:
        # Вычисляем производную в текущей точке
        fpx = f_prime(x_current)
        
        # Проверяем, не равна ли производная нулю
        if abs(fpx) < 1e-15:
            return None
        
        # Вычисляем следующее приближение
        x_next = x_current - f(x_current) / fpx
        
        # Увеличиваем счетчик итераций
        iterations += 1
        
        # Проверяем условие сходимости для нового приближения
        if abs(f(x_next)) < epsilon:
            return x_next, iterations
        
        x_current = x_next
    
    return None

def main():
    # Чтение входных данных из файла
    try:
        with open('input.txt', 'r', encoding='utf-8') as file:
            # Читаем коэффициенты функции
            coefficients = list(map(float, file.readline().strip().split()))
            a, b, c = coefficients
            
            # Читаем начальное приближение
            x0 = float(file.readline().strip())
            
            # Читаем допустимую погрешность
            epsilon = float(file.readline().strip())
    except:
        print("Solution not found")
        return
    
    # Проверяем, что a ≠ 0 (квадратичная функция)
    if abs(a) < 1e-15:
        print("Solution not found")
        return
    
    # Выполняем метод Ньютона
    result = newton_method(a, b, c, x0, epsilon)
    
    # Выводим результат
    if result is not None:
        root, iterations = result
        print(f"Root found: x = {root:.6f}")
        print(f"Number of iterations: {iterations}")
    else:
        print("Solution not found")


if __name__ == "__main__":
    main()