class CC:
    def __init__(self, g):
        self.marked = [False] * g.V
        self.id = [-1] * g.V
        self.size = [0] * g.V
        self.count = 0

        for v in range(g.V):
            if not self.marked[v]:
                self._dfs(g, v)
                self.count += 1

    def _dfs(self, g, v):
        self.marked[v] = True
        self.id[v] = self.count
        self.size[self.count] += 1

        for w in g.adj[v]:
            if not self.marked[w]:
                self._dfs(g, w)

    def connected(self, v, w):
        return self.id[v] == self.id[w]

    def component_vertices(self, component_id):
        vertices = []
        for v in range(len(self.id)):
            if self.id[v] == component_id:
                vertices.append(v)
        return vertices
