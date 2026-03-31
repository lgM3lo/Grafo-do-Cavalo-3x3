class Cycle:
    def __init__(self, g):
        self.marked = [False] * g.V
        self.edge_to = [-1] * g.V
        self.cycle = None

        for v in range(g.V):
            if not self.marked[v] and self.cycle is None:
                self._dfs(g, -1, v)

    def _dfs(self, g, parent, v):
        self.marked[v] = True

        for w in g.adj[v]:
            if self.cycle is not None:
                return

            if not self.marked[w]:
                self.edge_to[w] = v
                self._dfs(g, v, w)
            elif w != parent:
                path = [w]
                x = v
                while x != w:
                    path.append(x)
                    x = self.edge_to[x]
                path.append(w)
                path.reverse()
                self.cycle = path
                return

    def has_cycle(self):
        return self.cycle is not None

    def cycle_vertices(self):
        if self.cycle is None:
            return []
        return self.cycle
