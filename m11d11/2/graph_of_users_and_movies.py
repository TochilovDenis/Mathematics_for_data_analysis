from sys import stdin

def main():
    with open("input.txt", encoding="UTF-8") as file_in:
        lines = file_in.readlines()
        users = lines[0].replace('\n','').split(' ')
        movies = lines[1].replace('\n','').split(' ')


        i = 2
        a = True
        u = 1
        while i < len(lines):
            mas = lines[i].replace('\n','').split(' ')
            for movie in movies:
                if movie not in mas:
                    a = False
            i += 1


        if a:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()