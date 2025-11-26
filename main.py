from collections import deque

def bfs_distances(graph, start):
    """
    Return a dictionary mapping each reachable node to its
    shortest distance (number of edges) from 'start'.
    """
    if start not in graph:
        return {}

    dist = {start: 0}
    queue = deque([start])

    while queue:
        node = queue.popleft()

        for neighbor in graph.get(node, []):
            if neighbor not in dist:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)

    return dist


def bfs_shortest_path(graph, start, goal):
    """
    Return the shortest path from start to goal using BFS.
    If no path exists, return an empty list.
    """
    if start not in graph or goal not in graph:
        return []

    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return []


def path_length(path):
    """Return number of edges in the path."""
    if not path:
        return 0
    return len(path) - 1


def is_valid_path(graph, path, start, goal):
    """Validate that a path is legal in the graph."""
    if not path:
        return start == goal

    if path[0] != start or path[-1] != goal:
        return False

    for a, b in zip(path, path[1:]):
        if b not in graph.get(a, []):
            return False

    return True


if __name__ == "__main__":
    sample_graph = {
        "Gate": ["Stage1", "Stage2"],
        "Stage1": ["Gate", "Stage3"],
        "Stage2": ["Gate"],
        "Stage3": ["Stage1"],
    }
    d = bfs_distances(sample_graph, "Gate")
    print("Distances from Gate:", d)
