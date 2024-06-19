class Graph:
    def __init__(self, nodes_list):
        self.nodes = nodes_list
        self.adjacency_dict = {}
        for node in self.nodes:
            self.adjacency_dict[node] = []

    def add_link(self,first_node,second_node):
        self.adjacency_dict[first_node].append(second_node)
        self.adjacency_dict[second_node].append(first_node)

    def bfs(self,start_node):
        visited = set()
        queue = [start_node]
        visited.add(start_node)
        for node in queue:
            for next_node in self.adjacency_dict[node]:
                if next_node not in visited:
                    queue.append(next_node)
                    visited.add(next_node)

    def find_distances(self, start_node):
        distances = {}

        queue = [start_node]
        distances[start_node] = 0

        for node in queue:
            distance = distances[node]
            for next_node in self.adjacency_dict[node]:
                if next_node not in distances:
                    queue.append(next_node)
                    distances[next_node] = distance + 1
        return distances
    
    def best_route(self, a, b):
        d = self.find_distances(a)
        return d[b]


g1 = Graph([i for i in range(12+1)])
g1.add_link(10,9)
g1.add_link(9,0)
g1.add_link(0,11)

g1.add_link(10,1)
g1.add_link(9,8)
g1.add_link(0,7)
g1.add_link(11,7)

g1.add_link(1,8)
g1.add_link(8,12)
g1.add_link(7,3)
g1.add_link(7,6)

g1.add_link(12,2)
g1.add_link(2,3)
g1.add_link(3,4)
g1.add_link(6,5)

g1.bfs(0)

d = g1.find_distances(0)

for entry in d:
    print(entry, ":", d[entry])