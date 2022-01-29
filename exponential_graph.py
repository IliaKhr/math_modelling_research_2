import networkx as nx
from random import choice, seed
seed(7)

def _random_subset(repeated_nodes, k):
    targets = set()
    while len(targets) < k:
        x = choice(repeated_nodes)
        targets.add(x)
    return targets

def exponential_graph(n, k=7):
    """
    n: number of nodes
    """
    G = nx.empty_graph(n)
    repeated_nodes = list(range(k))
    targets = list(range(k))
    for source in range(k, n):
        G.add_edges_from(zip([source]*k, targets))
        repeated_nodes.extend([source])
        targets = _random_subset(repeated_nodes, k)
    return G
