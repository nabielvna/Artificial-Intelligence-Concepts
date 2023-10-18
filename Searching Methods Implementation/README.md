# Code Explanation

## Table of Contents
1. [Class](#1.-class)
   - [Node Class](#1.1-node-class)
   - [Graph Class](#1.2-graph-class)
       + [add_node](#add_node)
       + [add_edge](#add_edge)
2. [Searching Methods](#searching-methods)
   - [Breadth-First Search](#breadth-first-search)
   - [Greedy Best-First Search](#greedy-best-first-search)
   - [A* (A star)](#a*)
3. [Graph and Heuristics](#graph-and-heuristic)
4. [Output](#output)
5. [Code Output](#code-output)

### 1. Class
#### 1.1 Node Class:

The Node class represents a vertex or node in a graph. Each node has a name, a list of neighbors (adjacent nodes), and a heuristic value.
```
class Node:
    def __init__(self, name):
        self.name = name
        self.adjacent = {}
        self.heuristic = 0

    def add_adjacent(self, node, cost):
        self.adjacent[node] = cost
```

#### 1.2 Graph Class:

The Graph class represents a graph data structure. The graph consists of a set of nodes. Each node can have neighbors (adjacent nodes) and a cost to reach those neighbors.
```
class Graph:
    def __init__(self):
        self.nodes = {}
```
##### add_node:

The add_node method adds a new node to the graph. If a node with the same name already exists in the graph, this method will not do anything.
```
  def add_node(self, name):
    self.nodes[name] = Node(name)
```

##### add_edge:

The add_edge method adds an edge (or connection) between two nodes with a specific cost. If a node with the given name does not already exist in the graph, add_edge will create it first.
```
  def add_edge(self, name1, name2, cost):
    if name1 not in self.nodes:
      self.add_node(name1)
    if name2 not in self.nodes:
      self.add_node(name2)
      self.nodes[name1].add_adjacent(self.nodes[name2], cost)
      self.nodes[name2].add_adjacent(self.nodes[name1], cost)
```

### 2. Searching Methods
#### 2.1 Breadth-first Search

This is an implementation of the Breadth-First Search algorithm. It searches for a path from the starting node to the destination node using a queue to process nodes in a sequential manner. This function returns the path from start to end.
```
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
```

#### 2.2 Greedy Best-First Search

Implementation of the Greedy Best-First Search algorithm. It uses a priority queue based on the heuristic values of each node. The goal is to find a path from the starting node to the destination node by selecting the node closest to the goal based on the heuristic.
```
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
```

#### 2.3 A*

Implementation of the A* algorithm. It is a more advanced version of Greedy Best-First Search that also takes into account the actual cost from the starting node to the current node (g_costs). This algorithm attempts to find a path from the starting node to the destination node with the minimum cost.
```
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
```

### Graph and Heuristics:

In the final part of the code, you create a graph object (graph) and define heuristics for each node in the form of a dictionary (heuristics).

### Output:

Finally, the code prints the results of executing the BFS, Greedy Best-First Search, and A* algorithms. So, the code is an implementation of various search algorithms to find paths in a weighted graph with specific heuristics.

### Code Output

Code output based on my input
```
1. BFS: ['Ponorogo', 'Magetan', 'Madiun', 'Ngawi', 'Nganjuk', 'Bojonegoro', 'Jombang', 'Lamongan', 'Surabaya']
2. Greedy Best-First Search: ['Ponorogo', 'Madiun', 'Nganjuk', 'Jombang', 'Surabaya']
3. A*: ['Ponorogo', 'Madiun', 'Nganjuk', 'Jombang', 'Bojonegoro', 'Lamongan', 'Gresik', 'Surabaya']
```
