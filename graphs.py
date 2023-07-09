from stacks import Stack
from queues import Queue
from priority_queue import MinPQ
import math
# Graphs
# Adjacency List - best for adding lots of nodes (vertices).
# Adjacency matrix - best for lots of connections (edges) and querying data.
# Main drawback of matrix is huge storage (O(n^2)). Main drawback of
# adjacency list is slow search if lots of vertex and edges (O(v) + O(e)).
# Big O: Adjacency List - Add vertex => O(1), add edge => O(1), Remove edge,
# or vertex => O(n). Query and storage O(n) i.e. last two depend on edge/
# vertices. Matrix - Add or remove vertex and storage O(n^2). Add edge,
# remove edge or query O(1) - as matrix table makes look ups very fast and
# adding edges needs no more space or calculation power.
# AL = Adjacency List, AM = Adjacency Matrix, D = Directed (one-way edges),
# U = Undirected (two-way edges), W = Weighted (edges have values - so can
# use BFS and DFS based on weight rather than order added), N = Not weighted


# Adjacency List Undirected Non Weighted Graph
class ALUNGraph:
    """
    Adjacency List Undirected Graph. Create a list which stores the vertices
    and edges of a graph.
    :return: List of values contained in the ALUN
    """
    def __init__(self):
        self.adjacency_list = {}

    def __repr__(self):
        return f"{self.adjacency_list}"

    # add a vertex (node) to hash table
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            # print(f"{vertex} added as a vertex.")

    # add an edge (connection) to a vertex
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            if vertex2 not in self.adjacency_list[vertex1]:
                self.adjacency_list[vertex1].append(vertex2)
                # print(f"Added edge between {vertex1} and {vertex2}.")
            if vertex1 not in self.adjacency_list[vertex2]:
                self.adjacency_list[vertex2].append(vertex1)
                # print(f"Added edge between {vertex2} and {vertex1}.")

    # remove an edge between vertex
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
                # print(f"Removed edge between {vertex1} and {vertex2}.")
            except ValueError:
                print(f"No edge found between {vertex1} and {vertex2}.")

    # remove a vertex (including all its edges)
    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            for v in self.adjacency_list[vertex]:
                self.remove_edge(vertex, v)
            self.adjacency_list.pop(vertex, None)
            # print(f"Removed {vertex}.")

    # depth first traversal of nodes - move from node to node until all
    # nodes explored - only backtrack if no further option
    # DFS - Recursively
    def dfs_rec(self, vertex):
        vertex_list = []
        vertex_visited = {}

        # helper function called recursively
        def traverse(ver):
            if ver in vertex_visited and vertex_visited[ver]:
                return
            vertex_visited[ver] = True
            vertex_list.append(ver)
            for v in self.adjacency_list[ver]:
                traverse(v)

        traverse(vertex)
        return vertex_list

    # DFS - Iteratively - Reverse order of recursive approach
    def dfs_iter(self, vertex):
        vertex_visited = []
        vertices_in_stack = Stack()
        vertices_in_stack.push(vertex)

        while len(vertices_in_stack) > 0:
            current = vertices_in_stack.pop()
            vertex_visited.append(current)

            for v in self.adjacency_list[current]:
                if v not in vertex_visited and v not in vertices_in_stack:
                    vertices_in_stack.push(v)

        return vertex_visited

    # breadth first traversal of nodes - explore all paths on one node then
    # move to next
    # Breadth First - same logic as DFS (iter) but queues instead of stacks
    def bfs(self, vertex):
        vertex_visited = []
        vertices_in_stack = Queue()
        vertices_in_stack.enqueue(vertex)

        while len(vertices_in_stack) > 0:
            current = vertices_in_stack.dequeue()
            vertex_visited.append(current)

            for v in self.adjacency_list[current]:
                if v not in vertex_visited and v not in vertices_in_stack:
                    vertices_in_stack.enqueue(v)

        return vertex_visited


# Adjacency List Directed Non Weighted Graph
class ALDNGraph:
    """
    Adjacency List Directed Graph. Create a list which stores the vertices
    and edges of a graph.
    :return: List of values contained in the ALDN
    """
    def __init__(self):
        self.adjacency_list = {}

    def __repr__(self):
        return f"{self.adjacency_list}"

    # add a vertex (node) to hash table
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            # print(f"{vertex} added as a vertex.")

    # add an edge (connection) to a vertex
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            if vertex2 not in self.adjacency_list[vertex1]:
                self.adjacency_list[vertex1].append(vertex2)
                # print(f"Added edge between {vertex1} and {vertex2}.")
            # if vertex1 not in self.adjacency_list[vertex2]:
            #     self.adjacency_list[vertex2].append(vertex1)
            #     # print(f"Added edge between {vertex2} and {vertex1}.")

    # remove an edge between vertex
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                # self.adjacency_list[vertex2].remove(vertex1)
                # print(f"Removed edge between {vertex1} and {vertex2}.")
            except ValueError:
                print(f"No edge found between {vertex1} and {vertex2}.")

    # remove a vertex (including all its edges)
    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            for v in self.adjacency_list[vertex]:
                self.remove_edge(vertex, v)
            self.adjacency_list.pop(vertex, None)
            # print(f"Removed {vertex}.")

    # depth first traversal of nodes - move from node to node until all
    # nodes explored - only backtrack if no further option
    # DFS - Recursively
    def dfs_rec(self, vertex):
        vertex_list = []
        vertex_visited = {}

        # helper function called recursively
        def traverse(ver):
            if ver in vertex_visited and vertex_visited[ver]:
                return
            vertex_visited[ver] = True
            vertex_list.append(ver)
            for v in self.adjacency_list[ver]:
                traverse(v)

        traverse(vertex)
        return vertex_list

    # DFS - Iteratively - Reverse order of recursive approach
    def dfs_iter(self, vertex):
        vertex_visited = []
        vertices_in_stack = Stack()
        vertices_in_stack.push(vertex)

        while len(vertices_in_stack) > 0:
            current = vertices_in_stack.pop()
            vertex_visited.append(current)

            for v in self.adjacency_list[current]:
                if v not in vertex_visited and v not in vertices_in_stack:
                    vertices_in_stack.push(v)

        return vertex_visited

    # breadth first traversal of nodes - explore all paths on one node then
    # move to next
    # Breadth First - same logic as DFS (iter) but queues instead of stacks
    def bfs(self, vertex):
        vertex_visited = []
        vertices_in_stack = Queue()
        vertices_in_stack.enqueue(vertex)

        while len(vertices_in_stack) > 0:
            current = vertices_in_stack.dequeue()
            vertex_visited.append(current)

            for v in self.adjacency_list[current]:
                if v not in vertex_visited and v not in vertices_in_stack:
                    vertices_in_stack.enqueue(v)

        return vertex_visited

    # DFS - Find all Paths
    def path_finder_dfs_rec(self, vertex, destination):
        paths = []
        current_path = []

        # helper function called recursively
        def traverse(ver, dest):
            current_path.append(ver)

            if ver == dest:
                # make copy or python will overwrite
                temp = current_path.copy()
                paths.append(temp)
            else:
                for v in self.adjacency_list[ver]:
                    traverse(v, dest)

            # pop last from list so current_path accurate
            current_path.pop()

        traverse(vertex, destination)
        return paths


# Adjacency List Undirected Weighted Graph
class ALUWGraph:
    """
    Adjacency List Undirected Weighted. Create a list which stores the
    vertices (value and weight) and edges of a graph.
    :return: List of values contained in the ALUW
    """
    def __init__(self):
        self.adjacency_list = {}

    def __repr__(self):
        return f"{self.adjacency_list}"

    # add an entire matrix to graph
    def add_matrix(self, dict):
        {self.add_vertex(k) for k in dict.keys()}
        for k,v in dict.items():
            for i,j in v.items():
                self.add_edge(k, i, j)


    # add a vertex (node) to hash table
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            # print(f"{vertex} added as a vertex.")

    # add an edge (connection) to a vertex
    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            for i in self.adjacency_list[vertex1]:
                if i["vertex"] == vertex2:
                    break
            else:
                self.adjacency_list[vertex1].append({"vertex": vertex2,
                                                    "weight": weight})
                # print(f"Added edge between {vertex1} and {vertex2}.")
            for j in self.adjacency_list[vertex2]:
                if j["vertex"] == vertex1:
                    break
            else:
                self.adjacency_list[vertex2].append({"vertex": vertex1,
                                                    "weight": weight})
                # print(f"Added edge between {vertex2} and {vertex1}.")

    # remove an edge between vertex
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            try:
                for i in self.adjacency_list[vertex1]:
                    if i["vertex"] == vertex2:
                        self.adjacency_list[vertex1].remove(i)
                        # break
                for j in self.adjacency_list[vertex2]:
                    if j["vertex"] == vertex1:
                        self.adjacency_list[vertex2].remove(j)
                        # return
                print(f"Removed edge between {vertex1} and {vertex2}.")
            except ValueError:
                print(f"No edge found between {vertex1} and {vertex2}.")

    # remove a vertex (including all its edges)
    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            while len(self.adjacency_list[vertex]) > 0:
                for v in self.adjacency_list[vertex]:
                    self.remove_edge(vertex, v["vertex"])

            self.adjacency_list.pop(vertex, None)
            print(f"Removed {vertex}.")

    # depth first traversal of nodes - move from node to node until all
    # nodes explored - only backtrack if no further option
    # DFS - Recursively
    def dfs_rec(self, vertex):
        vertex_list = []
        vertex_visited = {}

        # helper function called recursively
        def traverse(ver):
            if ver in vertex_visited and vertex_visited[ver]:
                return
            vertex_visited[ver] = True
            vertex_list.append(ver)
            for v in self.adjacency_list[ver]:
                traverse(v["vertex"])

        traverse(vertex)
        return vertex_list

    # DFS - Iteratively - Reverse order of recursive approach
    def dfs_iter(self, vertex):
        vertex_visited = []
        vertices_in_stack = Stack()
        vertices_in_stack.push(vertex)

        while len(vertices_in_stack) > 0:
            current = vertices_in_stack.pop()
            vertex_visited.append(current)

            for v in self.adjacency_list[current]:
                if v["vertex"] not in vertex_visited and v["vertex"] not in \
                        vertices_in_stack:
                    vertices_in_stack.push(v["vertex"])

        return vertex_visited

    # breadth first traversal of nodes - explore all paths on one node then
    # move to next
    # Breadth First - same logic as DFS (iter) but queues instead of stacks
    def bfs(self, vertex):
        vertex_visited = []
        vertices_in_stack = Queue()
        vertices_in_stack.enqueue(vertex)

        while len(vertices_in_stack) > 0:
            current = vertices_in_stack.dequeue()
            vertex_visited.append(current)

            for v in self.adjacency_list[current]:
                if v["vertex"] not in vertex_visited and v["vertex"] not in \
                        vertices_in_stack:
                    vertices_in_stack.enqueue(v["vertex"])

        return vertex_visited

    # Dijkstra's algorithm - find shortest path in a weight undirected graph
    # using a priority queue system
    def dijkstra(self, start, end):
        # hash table to store routes
        distances = {k: (0 if k == start else math.inf) for k, v in
                     self.adjacency_list.items()}
        previous = {k: None for k, v in self.adjacency_list.items()}

        # path to be returned at end with final distance as a tuple
        path = []

        # min priority queue to get shortest path
        pq = MinPQ()
        pq.enqueue_all([(k, 0) if k == start else (k, math.inf) for k in
                        self.adjacency_list])

        while len(pq):
            # dequeue start node and store it's value
            node = pq.dequeue().value
            # once target dequeued can stop
            if node == end:
                while previous[node]:
                    path.append(node)
                    node = previous[node]
                path.append(start)
                break

            if node or distances[node] != math.inf:
                # loop through nodes neighbors calculating path as you go
                for neighbor in self.adjacency_list[node]:
                    # calculate new dist to neighboring node
                    candidate = distances[node] + neighbor["weight"]
                    # if candidate smaller than distance table => add
                    if candidate < distances[neighbor["vertex"]]:
                        # updating new smallest distance to neighbor
                        distances[neighbor["vertex"]] = candidate
                        # updating previous - how we got to neighbor
                        previous[neighbor["vertex"]] = node
                        # enqueue in priority queue with new priority
                        pq.enqueue(neighbor["vertex"], candidate)

        return f"The shortest distance from {start} to {end} is" \
               f" {distances[end]}", path[::-1]

    # Prim's algroithm for finding minimum spanning tree (MST) of a graph
    # Time complexity: O(log(n)). Form a tree that includes every vertex
    # with the minimum weight. Greedy algorith i.e. finds local optimum in
    # hope of finding global optimum
    def prims(self):
        pass

    # Kruskal's algroithm for finding minimum spanning tree (MST) of a graph
    # sort all edges from low weight to high and keep adding lowest edges
    # ignoring edges which create a cycle
    def kruskal(self):
        pass


# aluw = ALUWGraph()
# aluw.add_vertex("A")
# aluw.add_vertex("B")
# aluw.add_vertex("C")
# aluw.add_vertex("D")
# aluw.add_vertex("E")
# aluw.add_vertex("F")
# aluw.add_edge("A", "B", 4)
# aluw.add_edge("A", "C", 2)
# aluw.add_edge("B", "E", 3)
# aluw.add_edge("C", "D", 2)
# aluw.add_edge("C", "F", 4)
# aluw.add_edge("D", "E", 3)
# aluw.add_edge("D", "F", 1)
# aluw.add_edge("E", "F", 1)
# print(aluw.adjacency_list)
# print(aluw.dijkstra("A", "E"))

# input_graph = {
#     "A": {"B": 5, "D": 3, "E": 12, "F": 5},
#     "B": {"A": 5, "D": 1, "G": 2},
#     "C": {"E": 1, "F": 16, "G": 2},
#     "D": {"A": 3, "B": 1, "E": 1, "G": 1},
#     "E": {"A": 12, "C": 1, "D": 1, "F": 2},
#     "F": {"A": 5, "C": 16, "E": 2},
#     "G": {"B": 2, "C": 2, "D": 1}
# }
# aluw = ALUWGraph()
# aluw.add_matrix(input_graph)
# # print(aluw)
# print(aluw.dijkstra("B", "C"))