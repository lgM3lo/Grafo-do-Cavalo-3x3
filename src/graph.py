from algs4.bag import Bag


class Graph:
    def __init__(self, v):
        self.V = int(v)
        self.E = 0
        self.adj = [Bag() for _ in range(self.V)]

    def __str__(self):
        lines = ["%d vertices, %d edges" % (self.V, self.E)]
        for v in range(self.V):
            neighbors = " ".join(str(w) for w in self.adj[v])
            lines.append("%d: %s" % (v, neighbors))
        return "\n".join(lines)

    def add_edge(self, v, w):
        v, w = int(v), int(w)
        self.adj[v].add(w)
        self.adj[w].add(v)
        self.E += 1

    def degree(self, v):
        return self.adj[v].size()

    def max_degree(self):
        max_deg = 0
        for v in range(self.V):
            max_deg = max(max_deg, self.degree(v))
        return max_deg

    def number_of_self_loops(self):
        count = 0
        for v in range(self.V):
            for w in self.adj[v]:
                if w == v:
                    count += 1
        return count // 2

    @classmethod
    def from_stream(cls, stream):
        V = int(stream.readline())
        E = int(stream.readline())
        g = cls(V)
        for _ in range(E):
            v, w = stream.readline().split()
            g.add_edge(v, w)
        return g
