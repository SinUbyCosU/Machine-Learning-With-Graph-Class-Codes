#Create a graph using edgelist 

vertices=['A', 'B', 'C', 'D', 'E']
edge_list=[('A','B'),('A','C'),('B','D'),('C','D'),('D','E')]
G=nx.Graph(edge_list)
nx.draw(G,with_labels=True)

"""Using Networkx / Igraph, create a directed graph having 5 nodes and 10
edges. You are free to choose the direction. Plot the created graph using
Matplotlib or similar types of library available in Python or R."""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

g=nx.DiGraph(edge_list)

nx.draw(g)

nx.draw_planar(g, with_labels=True, node_color='lightblue')
nx.draw_circular(g,with_labels=True, node_color='lightgreen')

"""Estimate the following from the above graph: 1. Number of nodes, 2. Number
of edges, 3. Number of connected components, 4. Diameter
."""

G.number_of_nodes()
G.number_of_edges()
nx.number_of_connected_components(G)
nx.diameter(G)

"""❏ Implement degree centrality, closeness centrality, betweenness centrality, and
eigenvector centrality in an undirected simple graph without using any
library. You are free to create a simple graph with 5 nodes and 10 edges"""

adj=[[0 if i==j else 1 for j in range(5)] for i in range(5)]

degree={i:sum(adj[i])/4 for i in range(5)}

closeness={i:4/ sum(1 for j in range(5) if j!=i) for i in range(5)}

betweenness={i:0 for i in range(5)}

vec=[1/math.sqrt(5)]*5
for _ in range(100):
    next_vec=[sum(adj[i][j]*vec[j] for j in range(5)) for i in range(5)]
    norm=math.sqrt(sum(x**2 for x in next_vec))
    vec=[v/ norm for v in next_vec]

eigenvector={i: vec[i] for i in range(5)}

print("Degree Centrality:", degree )
print("Closeness Centrality:", closeness)
print("Betweenness Centrality:", betweenness)   
print("Eigenvector Centrality:", eigenvector)

"""Using Networkx or Igraph implement implement the above centrality
measures in the same graph. Compare the time required by your
implementation and the library version."""

nx.degree_centrality(g)
nx.closeness_centrality(g)
nx.betweenness_centrality(g)
nx.eigenvector_centrality(g)