from sys import stdin

def main():
    loop = False
    file_in = open("input.txt", encoding='UTF-8')
    n=[]
    for line in file_in:
        n.append(line.replace('\n', '').split(' '))
    file_in.close()

    for i in range(len(n)):
        if(n[i][i] == '1'):
            print(i)
            loop = True


    if(loop==False):
        print("NO LOOPS")


if __name__ == '__main__':
    main()