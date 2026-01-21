from graph_model import build_city_transport_graph, analyze_graph, visualize_graph
from traversals import bfs_path, dfs_path
from dijkstra import dijkstra, shortest_path, all_pairs_dijkstra


def main():
    G = build_city_transport_graph()

    # Task 1
    stats = analyze_graph(G)
    visualize_graph(G, "output/graph.png")

    print("TASK 1: Graph analysis")
    print("Nodes:", stats["nodes"])
    print("Edges:", stats["edges"])
    print("Connected:", stats["connected"])
    print("Max degree node:", stats["max_degree_node"])
    print("Min degree node:", stats["min_degree_node"])
    print("Degrees:", stats["degrees"])
    print("Graph saved to: output/graph.png\n")

    # Task 2
    start, goal = "Suburb", "Airport"
    bfs = bfs_path(G, start, goal)
    dfs = dfs_path(G, start, goal)

    print("TASK 2: BFS vs DFS paths")
    print(f"Start: {start} -> Goal: {goal}")
    print("BFS path:", bfs)
    print("DFS path:", dfs)
    print()

    # Task 3
    print("TASK 3: Dijkstra shortest paths")
    source = "Suburb"
    dist, prev = dijkstra(G, source)
    print(f"From source: {source}")
    for target in G.nodes:
        path = shortest_path(prev, target)
        print(f"  to {target:10s}: dist={dist[target]:5.1f}, path={path}")

    print("\nAll-pairs distances (summary):")
    all_dist = all_pairs_dijkstra(G)
    samples = [("Center", "Airport"), ("OldTown", "River"), ("Station", "Mall")]
    for s, t in samples:
        print(f"  {s} -> {t}: {all_dist[s][t]:.1f}")


if __name__ == "__main__":
    main()
