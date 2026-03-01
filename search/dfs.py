import time


def dfs(graph, start, goal):
    """
    Depth-First Search implementation.
    Returns metrics for evaluation.
    """

    start_time = time.perf_counter()

    stack = [(start, [start])]
    visited = set()

    visited_count = 0

    while stack:
        current_node, path = stack.pop()
        visited_count += 1

        if current_node == goal:
            end_time = time.perf_counter()
            return {
                "algorithm": "DFS",
                "path": path,
                "path_length": len(path) - 1,
                "visited_nodes": visited_count,
                "execution_time": end_time - start_time
            }

        if current_node not in visited:
            visited.add(current_node)

            for neighbor in graph.neighbors(current_node):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    end_time = time.perf_counter()
    return {
        "algorithm": "DFS",
        "path": None,
        "path_length": None,
        "visited_nodes": visited_count,
        "execution_time": end_time - start_time
    }