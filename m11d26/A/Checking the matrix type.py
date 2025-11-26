def main():
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())
        matrix = []
        for _ in range(n):
            row = list(map(float, f.readline().split()))
            matrix.append(row)

        violations = [0, 0, 0]  # [диагональная, верхняя, нижняя]
        
        for i in range(n):
            for j in range(n):
                if matrix[i][j] != 0:
                    if i != j:
                        violations[0] += 1
                    if i > j:
                        violations[1] += 1
                    if i < j:
                        violations[2] += 1
        
        if violations[0] == 0:
            print("DIAGONAL")
        elif violations[1] == 0:
            print("UPPER_TRIANGULAR")
        elif violations[2] == 0:
            print("LOWER_TRIANGULAR")
        else:
            print("OTHER")

if __name__ == "__main__":
    main()