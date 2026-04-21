from algs4.graph import Graph

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