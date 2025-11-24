def main():
    with open('input.txt', 'r') as f:
        mas = []
        k = int(f.readline().strip())        
        lymd = list(map(float, f.readline().strip().split()))
               
        for i in range(k):
            n = list(map(float, f.readline().strip().split()))
            if i == 0:
                mas = [0]*len(n)
            
            for y in range(len(n)):
                mas[y] += n[y] * lymd[i]

        
        for var in mas:
            print(f'{var:.2f}', end= ' ')



if __name__ == "__main__":
    main()
