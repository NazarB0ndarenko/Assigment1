from graph.generator import (
    generate_sparse_graph,
    generate_medium_graph,
    generate_dense_graph,
    get_random_start_goal
)

from search.bfs import bfs
from search.dfs import dfs


def print_results(dataset_name, bfs_result, dfs_result):
    print(f"\n===== {dataset_name} =====")

    print("\nBFS Result:")
    print(f"Visited Nodes: {bfs_result['visited_nodes']}")
    print(f"Path Length: {bfs_result['path_length']}")
    print(f"Execution Time: {bfs_result['execution_time']:.6f} seconds")

    print("\nDFS Result:")
    print(f"Visited Nodes: {dfs_result['visited_nodes']}")
    print(f"Path Length: {dfs_result['path_length']}")
    print(f"Execution Time: {dfs_result['execution_time']:.6f} seconds")

    print("\n---------------------------")


def run_dataset(dataset_name, graph):
    start, goal = get_random_start_goal(graph)

    print(f"\nStart node: {start}")
    print(f"Goal node: {goal}")

    bfs_result = bfs(graph, start, goal)
    dfs_result = dfs(graph, start, goal)

    print_results(dataset_name, bfs_result, dfs_result)


def main():
    datasets = [
        ("Sparse Graph", generate_sparse_graph()),
        ("Medium Graph", generate_medium_graph()),
        ("Dense Graph", generate_dense_graph())
    ]

    for name, graph in datasets:
        run_dataset(name, graph)


if __name__ == "__main__":
    main()