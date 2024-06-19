def factors(n):
    res = []
    i = 2
    while i<=n/2:
        if n % i == 0: res.append(i)
        i+=1
    return res

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

# Create the graph
graph1 = Graph([i for i in range(2,1000+1)])
for entry in graph1.nodes:
    for f in factors(entry):
        graph1.vertex(entry,f)

res = 0
for node in graph1.nodes:
    # Traverse the graph
    if graph1.visited[node]:
        continue
    else:
        traverse(graph1, 2)
        res+= 1
print(res)

