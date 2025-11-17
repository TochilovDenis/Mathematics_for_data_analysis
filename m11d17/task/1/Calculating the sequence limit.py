def main():
    with open("input.txt", encoding="UTF-8") as file_in:
        lines = file_in.readlines()
        n = int(lines[0])

        print(n/(n+1))


if __name__ == '__main__':
    main()