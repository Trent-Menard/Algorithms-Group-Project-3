# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 21:33:32 2022

@author: Dallas McAllister
"""
#source code
#https://www.youtube.com/watch?v=xREnpVUbkFI

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Use same seed for each generation (don't randomize)
seed = 4
np.random.seed(seed)

G = nx.DiGraph()
#setting the edges of the graph
G.add_edges_from([ ('4', '12'), ('4', '1'), ('1', '3')])

#the inner edges of the graph
G.add_edges_from([ ('4', '2'), ('2', '1'), ('3', '2')])

#the outer edges of the graph
G.add_edges_from([ ('3', '5'), ('5', '6'), ('6', '7')])

#the inner edges of the graph
G.add_edges_from([ ('5', '8'), ('6', '8'), ('8', '10')])
G.add_edges_from([ ('8', '9'), ('9', '5'), ('9', '11')])

#the outer edges of the graph
G.add_edges_from([ ('7', '10'), ('10', '11'), ('11', '12')])

#displaying the graph
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=200)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
nx.draw_networkx_labels(G, pos)
plt.show()
