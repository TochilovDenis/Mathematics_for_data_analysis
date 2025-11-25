import math


def main():
    with open('input.txt', 'r') as f:
        
        n = int(f.readline())
        u = list(map(float, f.readline().strip().split()))
        v = list(map(float, f.readline().strip().split()))
        u_ = 0
        v_ = 0
        scl = 0        
        for i in range(n):
            scl += u[i] * v[i]
            u_ += abs(u[i]) * abs(u[i])
            v_ += abs(v[i]) * abs(v[i])

        if scl != 0:
            cos = scl / (math.sqrt(u_) * math.sqrt(v_))
        else:
            cos = 0

        print(int(math.degrees(math.acos(cos))))


if __name__ == "__main__":
    main()
