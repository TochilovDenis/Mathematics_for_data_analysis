def f(x, func_str):
    """Вычисляет значение функции по строковому выражению"""
    if(func_str == ''):
         return eval(func_str.replace('x', str(x)))
    else:
        return eval(func_str)

def main():
    with open("input.txt", encoding="UTF-8") as file_in:
        lines = file_in.readlines()
            
        # Читаем входные данные
        func_str = lines[0].strip()
        x0 = float(lines[1].strip())
        delta = float(lines[2].strip())
            
        # Проверяем корректность входных данных
        if delta <= 0:
            raise ValueError("delta должно быть положительным числом")
            
        # Вычисляем допуск
        epsilon = 5 * delta
            
        # Вычисляем значения функции
        fx0 = f(x0, func_str)
        fx0_minus_delta = f(x0 - delta, func_str)
        fx0_plus_delta = f(x0 + delta, func_str)
            
        # Проверяем условия непрерывности
        left_condition = abs(fx0_minus_delta - fx0) < epsilon
        right_condition = abs(fx0_plus_delta - fx0) < epsilon
            
        # Выводим результат
        if left_condition and right_condition:
            print("CONTINUOUS")
        else:
            print("DISCONTINUOUS")


if __name__ == '__main__':
    main()