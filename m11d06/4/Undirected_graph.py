def main():
    with open("input_c1.txt", encoding="UTF-8") as file_in:
        lines = file_in.readlines()
        
        n = int(lines[0].strip())
        
        s, t = map(int, lines[-1].split())
        
        graph = []
        for i in range(1, len(lines) - 1):
            row = list(map(int, lines[i].strip().split()))
            graph.append(row)
    
    def bfs_shortest_path(start, target):
        if start == target:
            return 0

        queue = []
        queue.append((start, 0))

        visited = [False] * n
        visited[start] = True
        
        while queue:
            current, distance = queue.pop(0)

            for neighbor in range(n):
                if graph[current][neighbor] == 1 and not visited[neighbor]:
                    if neighbor == target:
                        return distance + 1
                    
                    visited[neighbor] = True
                    queue.append((neighbor, distance + 1))
        return -1
    
    result = bfs_shortest_path(s, t)
    print(result)


if __name__ == '__main__':
    main()