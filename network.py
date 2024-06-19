class Network:
    def __init__(self, nodes_max):
        self.nodes = [i+1 for i in range(nodes_max)]
        self.adjacency_dict = {}
        for node in self.nodes:
            self.adjacency_dict[node] = []

    def add_link(self,first_node,second_node):
        self.adjacency_dict[first_node].append(second_node)
        self.adjacency_dict[second_node].append(first_node)

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
        if b not in d: return -1
        else:
            return d[b]


if __name__ == "__main__":
    w = Network(5)
    w.add_link(1, 2)
    w.add_link(2, 3)
    w.add_link(1, 3)
    w.add_link(4, 5)
    print(w.best_route(1, 5)) # -1
    w.add_link(3, 5)
    print(w.best_route(1, 5)) # 2