import networkx as nx
import matplotlib.pyplot as plt


def ask_graph_type():
    graph_type = input("Podaj typ grafu (skierowany, nieskierowany, ważony): ")
    return graph_type


def ask_vertices():
    vertices = int(input("Podaj ilość wierzchołków: "))
    return vertices


def ask_edges():
    edges = int(input("Podaj ilość krawędzi: "))
    return edges


def ask_edge_data(graph_type):
    from_vertex = int(input("Podaj początek krawędzi: "))
    to_vertex = int(input("Podaj koniec krawędzi: "))
    if graph_type == "ważony":
        weight = float(input("Podaj wagę krawędzi: "))
        return (from_vertex, to_vertex, weight)
    else:
        return (from_vertex, to_vertex)


def create_graph(graph_type, vertices, edges):
    if graph_type == "skierowany":
        G = nx.DiGraph()
    else:
        G = nx.Graph()

    for v in range(vertices):
        G.add_node(v)

    for e in range(edges):
        edge_data = ask_edge_data(graph_type)
        G.add_edge(*edge_data)

    return G


def draw_graph(G):
    nx.draw(G, with_labels=True)
    plt.show()


def print_adjacency_matrix(G):
    print("Macierz sąsiedztwa: ")
    print(nx.adjacency_matrix(G).todense())


def print_adjacency_list(G):
    print("Lista sąsiedztwa: ")
    print(nx.generate_adjlist(G))


def main():
    graph_type = ask_graph_type()
    vertices = ask_vertices()
    edges = ask_edges()
    G = create_graph(graph_type, vertices, edges)
    print_adjacency_matrix(G)
    print_adjacency_list(G)
    draw_graph(G)


if __name__ == "__main__":
    main()
