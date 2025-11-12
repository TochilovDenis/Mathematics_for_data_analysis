import heapq

def dijkstra(graph, start):
    distance = {vertex: float('inf') for vertex in graph}
    distance[start] = 0
    priority_queue = [(0, start)]  # (расстояние, вершина)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Если найден более короткий путь, пропускаем
        if current_distance > distance[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance_to_neighbor = current_distance + weight

            if distance_to_neighbor < distance[neighbor]:
                distance[neighbor] = distance_to_neighbor
                heapq.heappush(priority_queue, (distance_to_neighbor, neighbor))

    return distance

# Пример использования
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

distances = dijkstra(graph, 'A')
print(distances)  # {'A': 0, 'B': 1, 'C': 3, 'D': 4}
