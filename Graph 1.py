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
# random.seed(seed)
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

nx.draw(G, with_labels=True, node_size=500, width=3, font_weight="bold", font_family="Times New Roman")
