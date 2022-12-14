"""
Created on Fri Oct 28 23:38:18 2022

@author: Trent

Helpful Links:
    https://networkx.org/documentation/stable/tutorial.html
    https://networkx.org/documentation/stable/reference/classes/index.html
    https://www.youtube.com/playlist?list=PLGZqdNxqKzfYXTwYAZIlmjnQmrytCSR1J
"""

import networkx as nx
import numpy as np

# Use same seed for each generation (don't randomize)
seed = 4
np.random.seed(seed)

G = nx.Graph()

nx.add_cycle(G, "AEFB")
G.add_edge("A", "F")
nx.add_path(G, "BCD")
nx.add_path(G, "AEIMN")
G.add_edge("I", "F")
G.add_edge("C", "G")
nx.add_path(G, "DGJI")

nx.add_cycle(G, "HKL")
G.add_edge("K","O")
G.add_edge("L", "P")

print()

# Perform DFS Traversal over edges from NetworkX
DFS_res = list(nx.edge_dfs(G))
print("DFS Results: " + str(len(DFS_res)) + " edges")
print(DFS_res)
print()

# Perform BFS Traversal over edges from NetworkX
BFS_res = list(nx.edge_bfs(G, source="A"))
print("BFS Results: " + str(len(BFS_res)) + " edges")
print(BFS_res)
print()
print()

print("Shortest Paths:")
shortest_paths = list(nx.shortest_simple_paths(G, source="A", target="B"))
for x in shortest_paths:
    print(x)

nx.draw(G, with_labels=True, node_size=500, width=3, font_weight="bold", font_family="Times New Roman")
