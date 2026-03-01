import networkx as nx
import random


def generate_sparse_graph():
    """
    Generates a sparse random graph with 25 nodes.
    Edge probability is low (0.1).
    """
    return nx.erdos_renyi_graph(n=25, p=0.1)


def generate_medium_graph():
    """
    Generates a medium-density random graph with 25 nodes.
    Edge probability is moderate (0.3).
    """
    return nx.erdos_renyi_graph(n=25, p=0.3)


def generate_dense_graph():
    """
    Generates a dense random graph with 25 nodes.
    Edge probability is high (0.6).
    """
    return nx.erdos_renyi_graph(n=25, p=0.6)


def get_random_start_goal(graph):
    """
    Selects two distinct random nodes from the graph.
    """
    nodes = list(graph.nodes())
    start = random.choice(nodes)
    goal = random.choice(nodes)

    while goal == start:
        goal = random.choice(nodes)

    return start, goal