class Coloring:
    def __init__(self, n):
        self.adjacency_dict = {i:[] for i in range(1,n+1)}

    def add_edge(self, a, b):
        self.adjacency_dict[a].append(b)
        self.adjacency_dict[b].append(a)

    def check(self):
        self.visited_nodes = set()
        for start_node in self.adjacency_dict:
            if start_node in self.visited_nodes: continue
            distances = {}
            queue = [start_node]
            distances[start_node] = 0

            for node in queue:
                self.visited_nodes.add(node)
                distance = distances[node]
                #print("Entering node", node)
                for next_node in self.adjacency_dict[node]:
                    if next_node not in distances:
                        queue.append(next_node)
                        distances[next_node] = distance + 1
                        #print("Added ", next_node, ": distances=", distances)
                    else:
                        #print(next_node, "is already in distances, diff=", distance - distances[next_node])
                        if (abs(distance - distances[next_node]) != 1):
                            return False
                #print("Leaving node", node)
        return True

if __name__ == "__main__":
#    c = Coloring(4)
#    c.add_edge(1, 2)
#    c.add_edge(2, 3)
#    c.add_edge(3, 4)
#    c.add_edge(1, 4)
#    print(c.check()) # True
#    c.add_edge(2, 4)
#    print(c.check()) # False

    c2 = Coloring(5)
    print(c2.check())
    print(c2.check())
    c2.add_edge(3,4)
    c2.add_edge(4,5)
    c2.add_edge(4,5)
    print(c2.check())
    c2.add_edge(4,5)
    c2.add_edge(3,5)
    print(c2.check())
    print(c2.check())
#    c1 = Coloring(11)
#    c1.add_edge(1,8)
#    c1.add_edge(8,2)
#    c1.add_edge(8,7)
#    c1.add_edge(2,3)
#    c1.add_edge(3,4)
#    c1.add_edge(2,5)
#    c1.add_edge(7,6)
#    c1.add_edge(5,6)
#    c1.add_edge(6,9)
#    c1.add_edge(7,11)
#    c1.add_edge(6,10)
#    c1.add_edge(11,10)
#    print(c1.check())