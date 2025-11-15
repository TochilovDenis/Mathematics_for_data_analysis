def main():
    with open("input.txt", encoding="UTF-8") as file_in:
        lines = file_in.readlines()

        n = int(lines[0])
        m = int(lines[2])

        if(n != m + 1):
            print("NO")
        else:
            print("YES")
       

if __name__ == '__main__':
    main()