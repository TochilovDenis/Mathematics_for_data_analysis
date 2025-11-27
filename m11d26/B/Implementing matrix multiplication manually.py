def main():
    with open('input.txt', 'r') as f:
        m, n = map(int, f.readline().split())
        mtr1 = []
        for i in range(m):
            mtr1.append(list(map(int, f.readline().split())))

        h, k = map(int, f.readline().split())
        mtr2 = []
        for i in range(h):
            mtr2.append(list(map(int, f.readline().split())))

        if n != h:
            print("NOT_DEFINED")
            return

        # mtr3 = [[0 for _ in range(k)] for _ in range(m)]
        mtr3 = []
        for i in range(m):      
            row = []           
            for j in range(k):
                row.append(0)
            mtr3.append(row)

        for i in range(m):
            for j in range(k):
                for l in range(n):
                    mtr3[i][j] += mtr1[i][l] * mtr2[l][j]

        for i in range(m):
            for j in range(k):
                print(mtr3[i][j], end=" ")
            print()


if __name__ == '__main__':
    main()