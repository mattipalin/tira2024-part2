class Cities:
    def __init__(self, n):
        self.nodes = [i for i in range(1,n+1)]
        self.vertices = {}
        self.visited = {}
        for node in self.nodes:
            self.vertices[node] = []
        self.reset_visited()

    def add_road(self, a, b):
        self.vertices[a].append(b)
        self.vertices[b].append(a)

    def traverse(self,node):
        if self.visited[node]:
            return
        self.visited[node] = True
        for neighbor in self.vertices[node]:
            self.traverse(neighbor)
            
    def reset_visited(self):
        for node in self.nodes:
            self.visited[node] = False

    def has_route(self, a, b):
        self.traverse(a)
        res = self.visited[b]
        self.reset_visited()
        return res


if __name__ == "__main__":
    c = Cities(5)
    c.add_road(1, 2)
    c.add_road(1, 3)
    c.add_road(4, 5)
    print(c.has_route(1, 5)) # False
    c.add_road(3, 4)
    print(c.has_route(1, 5)) # True