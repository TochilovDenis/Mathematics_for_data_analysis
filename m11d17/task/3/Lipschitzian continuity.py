import math


def main():
    with open("input.txt", encoding="UTF-8") as file_in:
        lines = file_in.readlines()

        env = { }                       # Словарь для передачи переменных в eval
        func_str = lines[0].strip()     # Считываем строку с функцией (например, "x**2")
        x1, x2 = lines[1].split(' ')    # Считываем границы интервала [a,b]
        x1 = float(x1)                  # Преобразуем в float
        x2 = float(x2)
        L = float(lines[2])             # Считываем константу Липшица L

        env['e'] = math.e               # Добавляем константу e в окружение для использования в функции

        # Вычисляем f(x1)
        env['x'] = x1                   # Устанавливаем x = x1 в окружении
        f_x1 = eval(func_str, env)      # Вычисляем значение функции в точке x1
        
        # Вычисляем f(x2)
        env['x'] = x2                   # Устанавливаем x = x2 в окружении
        f_x2 = eval(func_str, env)      # Вычисляем значение функции в точке x2
        

        # Условие Липшица: |f(x1)-f(x2)| <= L*|x1-x2|
        if abs(f_x1 - f_x2) < L * (abs(x1 - x2)):
            print("LIPSCHITZ")
        else:
            print("NOT LIPSCHITZ")



if __name__ == '__main__':
    main()

