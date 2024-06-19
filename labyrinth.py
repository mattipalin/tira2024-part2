class Graph:
    def __init__(self,nodes=[]):
        self.nodes = nodes
        self.vertices = {}
        self.visited = {}
        for node in nodes:
            self.vertices[node] = []
            self.visited[node] = False
    def vertex(self, a,b):
        self.vertices[a].append(b)
        self.vertices[b].append(a)
    def find_distances(self, start_node):
        distances = {}
        queue = [start_node]
        distances[start_node] = 0

        for node in queue:
            distance = distances[node]
            for next_node in self.vertices[node]:
                if next_node not in distances:
                    queue.append(next_node)
                    distances[next_node] = distance + 1
        return distances

def count(r):
    # Ihan aluksi gridin koko
    w = 0
    for el in r: w = max(w, len(el))
    node_list = []
    a_index = 0
    b_index = 0
    i = 0
    for row in r:
        for char in row:
            if(char=="."): node_list.append(i)
            if(char=="A"):
                node_list.append(i)
                a_index = i
            if(char=="B"):
                node_list.append(i)
                b_index = i
            i += 1
    g = Graph(node_list)

    # Sitten käydään kaikki noodit taas läpi ja lisätään naapurit
    for index in node_list:
        row = index // w
        col = index % w
        if(row*w+col+1 in node_list):
            g.vertex(row*w+col, row*w+col+1)
        if((row+1)*w+col in node_list):
            g.vertex((row+0)*w+col, (row+1)*w+col)


    d = g.find_distances(a_index)
    if b_index not in d: return -1
    else:
        return d[b_index]

if __name__ == "__main__":
    r = ["########",
         "#.A....#",
         "#.#.##.#",
         "#.##...#",
         "#...B#.#",
         "########"]
    print(count(r)) # 7