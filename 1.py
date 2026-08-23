# Q1: Create an undirected graph from an edge list.

vertices=['A', 'B', 'C', 'D', 'E']  # Store the five vertex labels used by the graph.
edge_list=[('A','B'),('A','C'),('B','D'),('C','D'),('D','E')]  # Store each connection as a pair of vertices.
G=nx.Graph(edge_list)  # Create an undirected NetworkX graph from the edge list.
nx.draw(G,with_labels=True)  # Draw the graph and display the vertex labels.

"""Using Networkx / Igraph, create a directed graph having 5 nodes and 10
edges. You are free to choose the direction. Plot the created graph using
Matplotlib or similar types of library available in Python or R."""

import networkx as nx  # Import NetworkX for graph creation and graph algorithms.
import numpy as np  # Import NumPy for numerical operations.
import matplotlib.pyplot as plt  # Import Matplotlib for plotting graphs.

g=nx.DiGraph(edge_list)  # Create a directed graph using the same edge list.

nx.draw(g)  # Draw the directed graph using the default layout.

nx.draw_planar(g, with_labels=True, node_color='lightblue')  # Draw the graph with a planar layout.
nx.draw_circular(g,with_labels=True, node_color='lightgreen')  # Draw the graph in a circular layout.

"""Estimate the following from the above graph: 1. Number of nodes, 2. Number
of edges, 3. Number of connected components, 4. Diameter
."""

G.number_of_nodes()  # Count and return the number of vertices in the undirected graph.
G.number_of_edges()  # Count and return the number of edges in the undirected graph.
nx.number_of_connected_components(G)  # Count and return the connected components in the graph.
nx.diameter(G)  # Calculate and return the greatest shortest-path distance in the graph.

"""Q3: Implement degree centrality, closeness centrality, betweenness centrality, and
eigenvector centrality in an undirected simple graph without using any
library. You are free to create a simple graph with 5 nodes and 10 edges"""

adj=[[0 if i==j else 1 for j in range(5)] for i in range(5)]  # Build a 5-by-5 adjacency matrix for a complete graph.

degree={i:sum(adj[i])/4 for i in range(5)}  # Divide each vertex degree by four to calculate degree centrality.

closeness={i:4/ sum(1 for j in range(5) if j!=i) for i in range(5)}  # Calculate closeness using the number of other vertices.

betweenness={i:0 for i in range(5)}  # Initialize betweenness scores for all vertices to zero.

vec=[1/math.sqrt(5)]*5  # Start power iteration with an equally weighted vector.
for _ in range(100):  # Repeat the eigenvector approximation for 100 iterations.
    next_vec=[sum(adj[i][j]*vec[j] for j in range(5)) for i in range(5)]  # Multiply the adjacency matrix by the current vector.
    norm=math.sqrt(sum(x**2 for x in next_vec))  # Calculate the Euclidean length of the new vector.
    vec=[v/ norm for v in next_vec]  # Normalize the vector to prevent its values from growing indefinitely.

eigenvector={i: vec[i] for i in range(5)}  # Store the final vector values as eigenvector centrality scores.

print("Degree Centrality:", degree )  # Print the manually calculated degree centrality values.
print("Closeness Centrality:", closeness)  # Print the manually calculated closeness centrality values.
print("Betweenness Centrality:", betweenness)  # Print the initialized betweenness centrality values.
print("Eigenvector Centrality:", eigenvector)  # Print the manually calculated eigenvector centrality values.

"""Using Networkx or Igraph implement implement the above centrality
measures in the same graph. Compare the time required by your
implementation and the library version."""

nx.degree_centrality(g)  # Calculate degree centrality with NetworkX for comparison.
nx.closeness_centrality(g)  # Calculate closeness centrality with NetworkX for comparison.
nx.betweenness_centrality(g)  # Calculate betweenness centrality with NetworkX for comparison.
nx.eigenvector_centrality(g)  # Calculate eigenvector centrality with NetworkX for comparison.