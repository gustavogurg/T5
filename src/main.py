from algs4.graph import Graph
from dsatur import dsatur

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

lista_cores = ["Vermelho", "Verde", "Azul", "Amarelo", "Ciano", "Magenta", "Laranja", "Roxo", "Marrom", "Cinza"]

for v in range(G.V):
    print('Coloração dos vértices:')
    print(f"Vértice {v} -> Cor {lista_cores[dsatur(G)[v]]}")
