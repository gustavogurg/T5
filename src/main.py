from algs4.graph import Graph


file_path ='../dados/brasil.txt'

def read_graph(file_path):
    with open(file_path, 'r') as f:
        V = int(f.readline().strip())
        E = int(f.readline().strip())

        G = Graph(V)

        edges_read = 0
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            if len(parts) < 2:
                continue

            v, w = map(int, parts[:2])
            G.add_edge(v, w)
            edges_read += 1

            if edges_read == E:
                break
    return G

def printGraph(G):
    print('Lista de adjascências:')
    print(f"{G.V} vertices, {G.E} arestas")
    for v in range(G.V):
        print(f"{v} ->", end=" ")
        node = G.adj[v].first
        while node is not None:
            print(node.item, end=" ")
            node = node.next
        print()

G = read_graph(file_path)
printGraph(G)

def dsatur(G):
    def vizinhos_de(v):
        viz = []
        node = G.adj[v].first
        while node is not None:
            viz.append(node.item)
            node = node.next
        return viz

    vertices = list(range(G.V))
    adj = {v: vizinhos_de(v) for v in vertices}

    cores = {v: None for v in vertices}
    saturacao = {v: 0 for v in vertices}
    graus = {v: len(adj[v]) for v in vertices}

    def cores_vizinhos(v):
        return {cores[u] for u in adj[v] if cores[u] is not None}

    atual = max(vertices, key=lambda v: graus[v])
    cores[atual] = 0

    for vizinho in adj[atual]:
        saturacao[vizinho] = len(cores_vizinhos(vizinho))

    while any(cores[v] is None for v in vertices):
        nao_coloridos = [v for v in vertices if cores[v] is None]

        atual = max(
            nao_coloridos,
            key=lambda v: (saturacao[v], graus[v])
        )

        usadas = cores_vizinhos(atual)
        cor = 0
        while cor in usadas:
            cor += 1

        cores[atual] = cor

        for vizinho in adj[atual]:
            if cores[vizinho] is None:
                saturacao[vizinho] = len(cores_vizinhos(vizinho))

    return cores

lista_cores = ["Vermelho", "Verde", "Azul", "Amarelo", "Ciano", "Magenta", "Laranja", "Roxo", "Marrom", "Cinza"]

for v in range(G.V):
    print(f"Vértice {v} -> Cor {lista_cores[dsatur(G)[v]]}")
