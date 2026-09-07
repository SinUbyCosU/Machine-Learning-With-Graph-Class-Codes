import networkx as nx
import matplotlib.pyplot as plt

graph=nx.read_edgelist("graphs_edges.txt", create_using=nx.DiGraph())
print(graph.nodes())
print(graph.edges())

nx.draw_networkx(graph, with_labels=True)
plt.show()