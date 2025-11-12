import networkx as nx
import random

random.seed(42) # Фиксируем состояние для воспроизводимости
graph = nx.erdos_renyi_graph(10, 0.3) # Создаём случайный граф с 10 вершинами и вероятностью ребра 0.3

# Считаем сумму степеней всех вершин
sum_degrees = sum(dict(graph.degree()).values())

# Считаем удвоенное количество рёбер
double_edges = 2 * graph.number_of_edges()

print(f"Сумма степеней: {sum_degrees}") # должно получиться 34
print(f"Удвоенное количество рёбер: {double_edges}") # должно получиться 34
