# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 09:18:21 2022

Graph 3 - Undirected weighted graph

Code adopted from:
    https://networkx.org/documentation/stable/auto_examples/drawing/plot_weighted_graph.html
    https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html
    https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.tree.mst.minimum_spanning_tree.html
@author: ryan-hasty
"""

import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
# Outer Perimeter
G.add_edge("A","B",weight=22)
G.add_edge("B","H",weight=34)
G.add_edge("H","I",weight=19)
G.add_edge("I","D",weight=30)
G.add_edge("D","A",weight=12)

# Connected vertices
G.add_edge("A","C",weight=9)
G.add_edge("C","B",weight=35)
G.add_edge("C","D",weight=4)
G.add_edge("B","F",weight=36)
G.add_edge("C","F",weight=42)
G.add_edge("C","E",weight=65)
G.add_edge("D","E",weight=33)
G.add_edge("E","F",weight=18)
G.add_edge("E","G",weight=23)
G.add_edge("F","G",weight=39)
G.add_edge("F","H",weight=24)
G.add_edge("G","I",weight=22)
G.add_edge("G","H",weight=22)

elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility

# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
nx.draw_networkx_edges(
G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
)


# node labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()

# Shortest path to all other nodes from A in G - using dijkstras
myShortest = nx.single_source_dijkstra_path_length(G,'A')
print("Shortest path from A to every other node in G\n\n", myShortest, "\n")

# Shortest path for all nodes to all othe nodes in G using dijkstras
print("Shortest path from each node in G to all other nodes in G for experimentation\n")
for x in G:    
    print("Starting from: ", x, " ",  nx.multi_source_dijkstra_path_length(G, x))
 
# Print MST
myMST = nx.minimum_spanning_tree(G, weight='weight')
print("\nMST \n\n", myMST.edges)