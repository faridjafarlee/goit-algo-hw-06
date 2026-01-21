import os
import networkx as nx
import matplotlib.pyplot as plt


def build_city_transport_graph() -> nx.Graph:
    """
    Реалістична модель транспортної мережі:
    вузли = локації (станції/перехрестя),
    ребра = дороги/маршрути,
    weight = умовний час/відстань (чим менше, тим краще).
    """
    G = nx.Graph()

    nodes = [
        "Center", "Station", "Park", "University", "Mall",
        "Hospital", "OldTown", "River", "Airport", "Suburb"
    ]
    G.add_nodes_from(nodes)

    weighted_edges = [
        ("Center", "Station", 4),
        ("Center", "Mall", 3),
        ("Center", "OldTown", 2),
        ("OldTown", "Park", 3),
        ("Park", "University", 2),
        ("University", "Mall", 4),
        ("Mall", "Hospital", 5),
        ("Hospital", "Station", 3),
        ("Station", "River", 6),
        ("River", "Airport", 7),
        ("Mall", "River", 4),
        ("Suburb", "Mall", 6),
        ("Suburb", "Park", 5),
        ("Suburb", "Airport", 10),
        ("OldTown", "Hospital", 6),
    ]

    for u, v, w in weighted_edges:
        G.add_edge(u, v, weight=w)

    return G


def analyze_graph(G: nx.Graph) -> dict:
    n_nodes = G.number_of_nodes()
    n_edges = G.number_of_edges()

    degrees = dict(G.degree())
    max_degree_node = max(degrees, key=degrees.get)
    min_degree_node = min(degrees, key=degrees.get)

    is_connected = nx.is_connected(G)

    return {
        "nodes": n_nodes,
        "edges": n_edges,
        "degrees": degrees,
        "max_degree_node": (max_degree_node, degrees[max_degree_node]),
        "min_degree_node": (min_degree_node, degrees[min_degree_node]),
        "connected": is_connected,
    }


def visualize_graph(G: nx.Graph, path: str = "output/graph.png") -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 7))

    nx.draw_networkx_nodes(G, pos, node_size=900)
    nx.draw_networkx_edges(G, pos, width=2)
    nx.draw_networkx_labels(G, pos, font_size=10)

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

    plt.axis("off")
    plt.tight_layout()
    plt.savefig(path, dpi=160)
    plt.close()
