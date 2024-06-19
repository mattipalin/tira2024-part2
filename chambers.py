def traverse(graph, node):
    if graph.visited[node]:
        return
    graph.visited[node] = True
    for neighbor in graph.vertices[node]:
        traverse(graph, neighbor)

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
    def print_graph(self):
        x = "{"
        for entry in self.vertices:
            x+=str(entry)+":"+str(self.vertices[entry])+","
        x+="}"
        print(x)


def count(r):
    # Ihan aluksi gridin koko
    w = 0
    for el in r: w = max(w, len(el))
    node_list = []
    i = 0
    for row in r:
        for char in row:
            if(char=="."): node_list.append(i)
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

    res = 0
    for node in g.nodes:
        if g.visited[node]: continue
        else:
            traverse(g, node)
            res+= 1
    return res

if __name__ == "__main__":
    r = ["########",
         "#..#...#",
         "####.#.#",
         "#..#.#.#",
         "########"]
    print(count(r)) # 3