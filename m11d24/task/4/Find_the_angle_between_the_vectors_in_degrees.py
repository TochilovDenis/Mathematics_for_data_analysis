import math

def main():
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        u = list(map(float, f.readline().strip().split()))
        v = list(map(float, f.readline().strip().split()))
        
        dot_product = 0
        u_norm = 0
        v_norm = 0
        
        for i in range(n):
            dot_product += u[i] * v[i]
            u_norm += u[i] * u[i]
            v_norm += v[i] * v[i]
        
        u_norm = math.sqrt(u_norm)
        v_norm = math.sqrt(v_norm)
        
        # Проверка на нулевые векторы
        if u_norm == 0 or v_norm == 0:
            print(0)
            return
        
        cos_angle = dot_product / (u_norm * v_norm)
        
        # Обеспечиваем, чтобы cos_angle был в допустимом диапазоне [-1, 1]
        cos_angle = max(-1.0, min(1.0, cos_angle))
        
        angle_rad = math.acos(cos_angle)
        angle_deg = math.degrees(angle_rad)
        
        # Округляем до целого путем отбрасывания дробной части
        print(int(angle_deg))

if __name__ == "__main__":
    main()