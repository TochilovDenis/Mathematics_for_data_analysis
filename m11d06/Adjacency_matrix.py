from sys import stdin

def main():
    file_in= open("input.txt", encoding='UTF-8')

    for line in file_in:
        n = line.replace('\n', '').split(' ')
        for i in range(len(n)):
            if(n[i] == '1'):
                print(i, end=' ')
        print()
    file_in.close()

if __name__ == '__main__':
    main()