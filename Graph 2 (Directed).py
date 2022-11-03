# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 21:33:32 2022

@author: Dallas McAllister
"""
#source code
#https://www.youtube.com/watch?v=xREnpVUbkFI
#Dr. Hu's code for SCC called scc.py
#Dr. Hu's code for topological order of a digraph

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import sys
import time
import heapq
#import resource
from itertools import groupby
from collections import defaultdict

#The first half of the program creates the DiGraph
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
#This marks the end of the first half of the program


#The second half of this program shows the strongly connected components
class Tracker(object):
    """Keeps track of the current time, current source, component leader,
    finish time of each node and the explored nodes.
    
    'self.leader' is informs of {node: leader, ...}."""

    def __init__(self):
        self.current_time = 0
        self.current_source = None
        self.leader = {}
        self.finish_time = {}
        self.explored = set()
        
def dfs(graph_dict, node, tracker):
    """Inner loop explores all nodes in a SCC. Graph represented as a dict,
    {tail: [head_list], ...}. Depth first search runs recursively and keeps
    track of the parameters"""

    tracker.explored.add(node)
    tracker.leader[node] = tracker.current_source
    for head in graph_dict[node]:
        if head not in tracker.explored:
            dfs(graph_dict, head, tracker)
    tracker.current_time += 1
    tracker.finish_time[node] = tracker.current_time
    
def dfs_loop(graph_dict, nodes, tracker):
    """Outer loop checks out all SCCs. Current source node changes when one
    SCC inner loop finishes."""

    for node in nodes:
        if node not in tracker.explored:
            tracker.current_source = node
            dfs(graph_dict, node, tracker)
            
def graph_reverse(graph):
    """Given a directed graph in forms of {tail:[head_list], ...}, compute
    a reversed directed graph, in which every edge changes direction."""

    reversed_graph = defaultdict(list)
    for tail, head_list in graph.items():
        for head in head_list:
            reversed_graph[head].append(tail)
    return reversed_graph

def scc(graph):
    """First runs dfs_loop on reversed graph with nodes in decreasing order,
    then runs dfs_loop on original graph with nodes in decreasing finish
    time order(obtained from first run). Return a dict of {leader: SCC}."""

    out = defaultdict(list)
    tracker1 = Tracker()
    tracker2 = Tracker()
    nodes = set()
    reversed_graph = graph_reverse(graph)
    for tail, head_list in graph.items():
        nodes |= set(head_list)
        nodes.add(tail)
    nodes = sorted(list(nodes), reverse=True)
    dfs_loop(reversed_graph, nodes, tracker1)
    sorted_nodes = sorted(tracker1.finish_time,
                          key=tracker1.finish_time.get, reverse=True)
    dfs_loop(graph, sorted_nodes, tracker2)
    for lead, vertex in groupby(sorted(tracker2.leader, key=tracker2.leader.get),
                                key=tracker2.leader.get):
        out[lead] = list(vertex)
    return out
def main():
    start = time.time()
    '''    graph = defaultdict(list)
    with open('SCC.txt') as file_in:
    #with open('test.txt') as file_in:
        for line in file_in:
            x = line.strip().split()
            x1, x2 = int(x[0]), int(x[1])
            graph[x1].append(x2)'''
    graph = {
          '1': set(['3']),
          '2': set(['1']),
          '3': set(['2', '5']),
          '4': set(['1', '2', '12']),
          '5': set(['6', '8']),
          '6': set(['7','8']),
          '7': set(['10']),
          '8': set(['9', '10']),
          '9': set(['5', '11']),
          '10': set(['11']),
          '11': set(['12']),
          '12': set()
             }
    t1 = time.time() - start
    print (t1)
    groups = scc(graph)
    t2 = time.time() - start
    print (round(t2,4))     
    top_5 = heapq.nlargest(5, groups, key=lambda x: len(groups[x]))
    #sorted_groups = sorted(groups, key=lambda x: len(groups[x]), reverse=True)
    result = []
    for i in range(5):
         try:
             result.append(len(groups[top_5[i]]))
             #result.append(len(groups[sorted_groups[i]]))
         except:
             result.append(0)
    return result, groups


if __name__ == '__main__':
     count, components = main()
print('Strongly connected components are:')
for key in components:
     print(components[key])
#This marks the end of the second half of the program

#This is the third part of the program,
#making the graph in topological order
def dfs_tpl_order(graph,start,path):
    path = path + [start]
    global n
    for edge in graph[start]: 
        if edge not in path:
            path = dfs_tpl_order(graph, edge,path)
    print (n, start)
    n -= 1
    return path
  

# Graphing the original in topological order
graph = {'1': set(['3']),
         '2': set(['1']),
         '3': set(['2', '5']),
         '4': set(['1', '2', '12']),
         '5': set(['6', '8']),
         '6': set(['7','8']),
         '7': set(['10']),
         '8': set(['9', '10']),
         '9': set(['5', '11']),
         '10': set(['11']),
         '11': set(['12']),
         '12': set()}
         
n = len(graph)
print('\nTopological order starting from \'1\'')
u = dfs_tpl_order(graph, '1', [])
print(u)
#This marks the end of the program
