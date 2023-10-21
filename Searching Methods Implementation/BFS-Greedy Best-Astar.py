import heapq

class Node:
    def __init__(self, name):
        self.name = name
        self.adjacent = {}

    def add_adjacent(self, node, cost):
        self.adjacent[node] = cost

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        self.nodes[name] = Node(name)

    def add_edge(self, name1, name2, cost):
        if name1 not in self.nodes:
            self.add_node(name1)
        if name2 not in self.nodes:
            self.add_node(name2)
        self.nodes[name1].add_adjacent(self.nodes[name2], cost)
        self.nodes[name2].add_adjacent(self.nodes[name1], cost)
    
#BFS
def bfs(graph, start, end):
    visited = set() 
    queue = [start]
    path = []

    while queue:
        current = queue.pop(0)
        if current in visited:
            continue
        path.append(current)
        if current == end:
            return path
        visited.add(current)
        for neighbour in graph.nodes[current].adjacent:
            queue.append(neighbour.name)

#Greedy Best
def greedy_best_first_search(graph, start, end, heuristics):
    visited = set()
    priority_queue = [(heuristics[start], start)]
    path = []

    while priority_queue:
        _, current = heapq.heappop(priority_queue)
        if current in visited:
            continue
        path.append(current)
        if current == end:
            return path
        visited.add(current)
        for neighbour in graph.nodes[current].adjacent:
            heapq.heappush(priority_queue, (heuristics[neighbour.name], neighbour.name))

#A*
def a_star(graph, start, end, heuristics):
    visited = set()
    priority_queue = [(heuristics[start], start)]
    g_costs = {node: float('infinity') for node in graph.nodes}
    g_costs[start] = 0
    path = []

    while priority_queue:
        _, current = heapq.heappop(priority_queue)
        if current in visited:
            continue
        path.append(current)
        if current == end:
            return path
        visited.add(current)
        for neighbour, cost in graph.nodes[current].adjacent.items():
            tentative_g = g_costs[current] + cost
            if tentative_g < g_costs[neighbour.name]:
                g_costs[neighbour.name] = tentative_g
                f = g_costs[neighbour.name] + heuristics[neighbour.name]
                heapq.heappush(priority_queue, (f, neighbour.name))

# Graph
graph = Graph()
graph.add_edge('Magetan', 'Ngawi', 32)
graph.add_edge('Magetan', 'Madiun', 22)
graph.add_edge('Magetan', 'Ponorogo', 34)
graph.add_edge('Surabaya', 'Gresik', 12)
graph.add_edge('Surabaya', 'Bangkalan', 44)
graph.add_edge('Surabaya', 'Sidoarjo', 25)
graph.add_edge('Surabaya', 'Jombang', 72)
graph.add_edge('Ngawi', 'Bojonegoro', 44)
graph.add_edge('Ngawi', 'Madiun', 30)
graph.add_edge('Ngawi', 'Magetan', 32)
graph.add_edge('Ponorogo', 'Magetan', 34)
graph.add_edge('Ponorogo', 'Madiun', 29)
graph.add_edge('Madiun', 'Ngawi', 30)
graph.add_edge('Madiun', 'Magetan', 22)
graph.add_edge('Madiun', 'Ponorogo', 29)
graph.add_edge('Madiun', 'Nganjuk', 48)
graph.add_edge('Bojonegoro', 'Ngawi', 44)
graph.add_edge('Bojonegoro', 'Nganjuk', 33)
graph.add_edge('Bojonegoro', 'Jombang', 70)
graph.add_edge('Bojonegoro', 'Lamongan', 42)
graph.add_edge('Nganjuk', 'Madiun', 48)
graph.add_edge('Nganjuk', 'Bojonegoro', 33)
graph.add_edge('Nganjuk', 'Jombang', 40)
graph.add_edge('Jombang', 'Nganjuk', 40)
graph.add_edge('Jombang', 'Bojonegoro', 70)
graph.add_edge('Jombang', 'Surabaya', 72)
graph.add_edge('Lamongan', 'Bojonegoro', 42)
graph.add_edge('Lamongan', 'Gresik', 14)
graph.add_edge('Gresik', 'Lamongan', 14)
graph.add_edge('Gresik', 'Surabaya', 12)
graph.add_edge('Sidoarjo', 'Surabaya', 25)
graph.add_edge('Sidoarjo', 'Probolinggo', 78)
graph.add_edge('Probolinggo', 'Sidoarjo', 78)
graph.add_edge('Probolinggo', 'Situbondo', 99)
graph.add_edge('Situbondo', 'Probolinggo', 99)
graph.add_edge('Bangkalan', 'Surabaya', 44)
graph.add_edge('Bangkalan', 'Sampang', 52)
graph.add_edge('Sampang', 'Bangkalan', 52)
graph.add_edge('Sampang', 'Pamekasan', 31)
graph.add_edge('Pamekasan', 'Sampang', 31)
graph.add_edge('Pamekasan', 'Sumenep', 54)
graph.add_edge('Sumenep', 'Pamekasan', 54)

# Heuristic
heuristics = {
    'Magetan': 162,
    'Surabaya': 0,
    'Ngawi': 130,
    'Ponorogo': 128,
    'Madiun': 126,
    'Bojonegoro': 60,
    'Nganjuk': 70,
    'Jombang': 36,
    'Lamongan': 36,
    'Gresik': 12,
    'Sidoarjo': 22,
    'Probolinggo': 70,
    'Situbondo': 146,
    'Bangkalan': 140,
    'Sampang': 90,
    'Pamekasan': 104,
    'Sumenep': 150
}

#Output
print("1. BFS:", bfs(graph, 'Ponorogo', 'Surabaya'))
print("2. Greedy Best-First Search:", greedy_best_first_search(graph, 'Ponorogo', 'Surabaya', heuristics))
print("3. A*:", a_star(graph, 'Ponorogo', 'Surabaya', heuristics))
