import heapq
import networkx as nx
from typing import Dict, Tuple, List, Optional


def dijkstra(G: nx.Graph, source: str) -> Tuple[Dict[str, float], Dict[str, Optional[str]]]:
    dist = {node: float("inf") for node in G.nodes}
    prev = {node: None for node in G.nodes}
    dist[source] = 0.0

    pq = [(0.0, source)]

    while pq:
        cur_d, u = heapq.heappop(pq)
        if cur_d != dist[u]:
            continue

        for v in G.neighbors(u):
            w = G[u][v].get("weight", 1)
            nd = cur_d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))

    return dist, prev


def shortest_path(prev: Dict[str, Optional[str]], target: str) -> List[str]:
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    return path


def all_pairs_dijkstra(G: nx.Graph) -> Dict[str, Dict[str, float]]:
    all_dist = {}
    for s in G.nodes:
        dist, _ = dijkstra(G, s)
        all_dist[s] = dist
    return all_dist
