from sys import stdin

def main():
    with open("input.txt", encoding="UTF-8") as file_in:
        lines = file_in.readlines()

        leaves=[]
        i=1
        while i < len(lines):
            line_n = lines[i].replace('\n', '').split(' ')
            num = 0
            for y in line_n:
                if y == '1':
                    num += 1
            if num == 1:
                leaves.append(i - 1)
            i += 1

        if len(leaves) == 0:
            print("NO LEAVES")

        for y in leaves:
           print(y)


if __name__ == '__main__':
    main()