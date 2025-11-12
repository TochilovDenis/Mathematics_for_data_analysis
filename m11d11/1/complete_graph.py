def main():
    with open("input.txt", encoding="UTF-8") as file_in:
        lines = file_in.readlines()
        v  = int(lines[0])
        print(int((v * (v - 1))/2))


if __name__ == '__main__':
    main()