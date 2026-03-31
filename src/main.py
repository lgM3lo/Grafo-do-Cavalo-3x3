import sys
from pathlib import Path
from collections import deque

from graph import Graph
from cc import CC
from cycle import Cycle


def position_to_vertex(row, col, n=3):
    return row * n + col


def bfs_shortest_path(g, source, target):
    marked = [False] * g.V
    dist_to = [-1] * g.V
    edge_to = [-1] * g.V

    queue = deque([source])
    marked[source] = True
    dist_to[source] = 0

    while queue:
        v = queue.popleft()

        for w in g.adj[v]:
            if not marked[w]:
                marked[w] = True
                edge_to[w] = v
                dist_to[w] = dist_to[v] + 1
                queue.append(w)

    if dist_to[target] == -1:
        return -1, []

    path = []
    x = target
    while x != -1:
        path.append(x)
        x = edge_to[x]
    path.reverse()

    return dist_to[target], path


def print_adjacency_list(g):
    for v in range(g.V):
        neighbors = " ".join(str(w) for w in g.adj[v])
        print(f"{v}: {neighbors}")


def resolve_input_path():
    if len(sys.argv) >= 2:
        input_path = Path(sys.argv[1])
        if input_path.exists():
            return input_path

        raise FileNotFoundError(
            f"Arquivo de entrada não encontrado: {sys.argv[1]}"
        )

    current_file = Path(__file__).resolve()
    candidates = [
        Path.cwd() / "dados" / "entrada.txt",
        current_file.parent.parent / "dados" / "entrada.txt",
        current_file.parent / ".." / "dados" / "entrada.txt",
    ]

    for candidate in candidates:
        candidate = candidate.resolve()
        if candidate.exists():
            return candidate

    raise FileNotFoundError(
        "Não foi possível localizar automaticamente o arquivo de entrada. "
        "Coloque 'dados/entrada.txt' na pasta do projeto ou execute: "
        "python src/main.py dados/entrada.txt"
    )


if __name__ == '__main__':
    try:
        input_path = resolve_input_path()
    except FileNotFoundError as error:
        print(error)
        sys.exit(1)

    with open(input_path, encoding='utf-8') as f:
        g = Graph.from_stream(f)

    print(f'Arquivo de entrada: {input_path}')
    print()
    print('Lista de adjacência:')
    print_adjacency_list(g)
    print()

    cc = CC(g)
    print(f'Componentes conexas: {cc.count}')
    for component_id in range(cc.count):
        vertices = cc.component_vertices(component_id)
        print(f"Vértices da componente {component_id}: {' '.join(map(str, vertices))}")
    print()

    source = position_to_vertex(0, 0)
    target = position_to_vertex(2, 2)
    distance, path = bfs_shortest_path(g, source, target)

    if distance == -1:
        print('Distância mínima entre (0,0) e (2,2): não existe caminho')
    else:
        print(f'Distância mínima entre (0,0) e (2,2): {distance}')
        print(f"Um caminho mínimo encontrado: {' '.join(map(str, path))}")
    print()

    cycle = Cycle(g)
    print(f"O grafo possui ciclo: {'Sim' if cycle.has_cycle() else 'Não'}")
    print('Complexidade da detecção de ciclo com DFS:')
    print('Tempo: O(V + E)')
    print('Espaço: O(V)')

    if cycle.has_cycle():
        print(f"Um ciclo encontrado: {' '.join(map(str, cycle.cycle_vertices()))}")
