import math


def main():
    with open("input.txt", encoding="UTF-8") as file_in:
        lines = file_in.readlines()

        a, b, c, d = list(map(float, lines[0].split()))
        p, q = list(map(float, lines[1].split()))
        
        # Находим критические точки
        critical_points = []
        
        # Производная: 3a*x^2 + 2b*x + c = 0
        A = 3 * a
        B = 2 * b
        C = c
        
        # Проверяем различные случаи
        if abs(A) < 1e-12:      # A ≈ 0 (линейная производная)
            if abs(B) < 1e-12:  # B ≈ 0 (постоянная функция)
                # f'(x) = C, если C ≠ 0 - нет критических точек
                pass
            else:  # Линейная производная: B*x + C = 0
                x = -C / B
                if p <= x <= q:
                    critical_points.append(x)
        else:  # Квадратное уравнение
            discriminant = B * B - 4 * A * C
            
            if discriminant > 0:  # Два различных корня
                sqrt_d = math.sqrt(discriminant)
                x1 = (-B - sqrt_d) / (2 * A)
                x2 = (-B + sqrt_d) / (2 * A)
                
                # Проверяем принадлежность интервалу
                if p <= x1 <= q:
                    critical_points.append(x1)
                if p <= x2 <= q:
                    critical_points.append(x2)
                    
            elif abs(discriminant) < 1e-12:  # Один корень (кратности 2)
                x = -B / (2 * A)
                if p <= x <= q:
                    critical_points.append(x)
            # Если discriminant < 0 - нет действительных корней
        
        # Сортируем критические точки
        critical_points.sort()
        
        # Выводим результаты
        if critical_points:
            for x in critical_points:
                # Вторая производная: 6a*x + 2b
                second_derivative = 6 * a * x + 2 * b
                
                # Определяем тип точки
                if abs(second_derivative) < 1e-12:
                    point_type = "Saddle point"
                elif second_derivative > 0:
                    point_type = "Local minimum"
                else:
                    point_type = "Local maximum"
                
                # Вычисляем значение функции
                fx = a * x**3 + b * x**2 + c * x + d
                
                # Выводим результат
                print(f"{point_type} at x = {x:.5f}")
                print(f"f(x) = {fx:.5f}")
        else:
            print("No critical points found.")


if __name__ == '__main__':
    main()