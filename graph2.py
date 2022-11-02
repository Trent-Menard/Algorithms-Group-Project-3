# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 21:33:32 2022

@author: DJMack
"""

import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()
G.add_edges_from([ ('4', '12'), ('4', '1'), ('1', '3')])
G.add_edges_from([ ('4', '2'), ('2', '1'), ('3', '2')])
G.add_edges_from([ ('3', '5'), ('5', '6'), ('6', '7')])
G.add_edges_from([ ('5', '8'), ('6', '8'), ('8', '10')])
G.add_edges_from([ ('8', '9'), ('9', '5'), ('9', '11')])
G.add_edges_from([ ('7', '10'), ('10', '11'), ('11', '12')])
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=400)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
nx.draw_networkx_labels(G, pos)
plt.show()