from collections import deque
import time


def bfs(graph, start, goal):
    """
    Breadth-First Search implementation.
    Returns metrics for evaluation.
    """

    start_time = time.perf_counter()

    queue = deque()
    queue.append((start, [start]))

    visited = set()
    visited.add(start)

    visited_count = 0

    while queue:
        current_node, path = queue.popleft()
        visited_count += 1

        if current_node == goal:
            end_time = time.perf_counter()
            return {
                "algorithm": "BFS",
                "path": path,
                "path_length": len(path) - 1,
                "visited_nodes": visited_count,
                "execution_time": end_time - start_time
            }

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    end_time = time.perf_counter()
    return {
        "algorithm": "BFS",
        "path": None,
        "path_length": None,
        "visited_nodes": visited_count,
        "execution_time": end_time - start_time
    }