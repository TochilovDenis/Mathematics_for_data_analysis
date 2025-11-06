from sys import stdin

def main():
    with open("input_c.txt", encoding="UTF-8") as file_in:
        lines = file_in.readlines()
        a = int(lines[0])

        n=[[0 for i in range(a)] for i in range(a)]

        i = 1
        while i < len(lines):
            mas=lines[i].replace('\n', '').split(' ')

            for var in mas:
                if var != '':
                    n[(i-1)][(int(var))] = 1

            i = i + 1

        for i in n:
            for j in i:
                print(j, end= " ")
            print()


if __name__ == '__main__':
    main()