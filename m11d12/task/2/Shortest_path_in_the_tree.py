def main():
    with open("input.txt", encoding="UTF-8") as file_in:
        lines = file_in.readlines()
        
        # Чтение количества вершин
        n = int(lines[0].strip())
        
        # Чтение матрицы смежности
        graph = [[] for _ in range(n)]
        for i in range(1, 1 + n):  # строки с 1 по n+1
            row = list(map(int, lines[i].split()))
            for j in range(n):
                if row[j] == 1:
                    graph[i-1].append(j)
        
        # Чтение начальной и конечной вершин
        r, v = map(int, lines[1 + n].split())
    
    # Поиск пути с помощью BFS (без deque)
    visited = [False] * n
    parent = [-1] * n  # для восстановления пути
    
    queue = [r]
    visited[r] = True
    front = 0  # указатель на начало очереди
    
    while front < len(queue):
        current = queue[front]
        front += 1
        
        # Если достигли целевую вершину
        if current == v:
            # Восстановление пути
            path = []
            node = v
            while node != -1:
                path.append(node)
                node = parent[node]
            path.reverse()
            print(' '.join(map(str, path)))
            return
        
        # Добавляем всех непосещенных соседей
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = current
                queue.append(neighbor)
    
    # Если путь не найден (в дереве такого быть не должно)
    print("NO PATH")


if __name__ == '__main__':
    main()