from sys import stdin

def main():
    with open("input.txt", encoding="UTF-8") as file_in:
        lines = file_in.readlines()
        
        a = int(lines[0])        
        s, t = lines[len(lines)-1].split(' ')
        s = int(s)
        t = int(t)
        gruph = []
        list_gruph = []
        
        i = 1
        while i < len(lines)-1:
            line_n = lines[i].replace('\n', '').split(' ')
            gruph.append(line_n)
            m_line = []
            for y in range(len(line_n)):
                if(line_n[y] == '1'):
                    #print(y, end=' ')
                    m_line.append(y)

            #print()
            list_gruph.append(m_line)
            i += 1

        used = [0] * a

        # gruph - список смежности
        # s - начальная вершина
        # t - вершина до которой ищем путь
        # used - список вершин в которых мы уже были  
        print(DFS(list_gruph, t, s, used, 0))


def DFS(list_gruph, t, v, used, go):
    used[v] = 1
    if v == t:
        used[v] = 0
        return go
    
    a =- 1
    # a =-1 конечная вершина еще не найдена 
    # 0 -> 1 -> 2 -> 4-x return -1
    # 0 -> 1 -> 2 -> 3 return 3
    # 0 -> 1 -> 2 x 1 пропускаем

    # 0 -> 1 -> 2 -> 3 return 3 used [1, 1, 1, 1, 0]
    # 0 -> 1 -> 2 <- 3 return 3 used [1, 1, 1, 0, 0]
    # 0 -> 1 <- 2 <- 3 return 3 used [1, 1, 0, 0, 0]
    # 0 <- 1 <- 2 <- 3 return 3 used [1, 0, 0, 0, 0]

    # 0 -> 3           return 1 used [1, 0, 0, 1,]

    for u in list_gruph[v]:
        if used[u] == 0:
           b = DFS(list_gruph, t, u, used, go + 1)
           if( b != -1):
               if(b < a or a == -1):
                   a = b
    used[v] = 0
    return a      

       
if __name__ == '__main__':
    main()