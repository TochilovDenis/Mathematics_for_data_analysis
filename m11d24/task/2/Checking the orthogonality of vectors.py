import math


def main():
    with open('input.txt', 'r') as f:
        
        n = int(f.readline())
        u = list(map(float, f.readline().strip().split()))
        v = list(map(float, f.readline().strip().split()))

        scl = 0        
        for i in range(n):
            scl += u[i] * v[i]

        if scl == 0:
            print("ORTHOGONAL")
        else:
            print("NON-ORTHOGONAL")


if __name__ == "__main__":
    main()
