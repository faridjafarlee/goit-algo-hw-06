from collections import deque
import networkx as nx
from typing import List, Optional


def bfs_path(G: nx.Graph, start: str, goal: str) -> Optional[List[str]]:
    if start == goal:
        return [start]

    visited = set([start])
    parent = {start: None}
    q = deque([start])

    while q:
        node = q.popleft()
        for nei in G.neighbors(node):
            if nei not in visited:
                visited.add(nei)
                parent[nei] = node
                if nei == goal:
                    return _reconstruct(parent, goal)
                q.append(nei)

    return None


def dfs_path(G: nx.Graph, start: str, goal: str) -> Optional[List[str]]:
    visited = set()
    parent = {start: None}

    def dfs(u: str) -> bool:
        visited.add(u)
        if u == goal:
            return True
        for nei in G.neighbors(u):
            if nei not in visited:
                parent[nei] = u
                if dfs(nei):
                    return True
        return False

    found = dfs(start)
    return _reconstruct(parent, goal) if found else None


def _reconstruct(parent: dict, goal: str) -> List[str]:
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path
