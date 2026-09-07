import networkx as nx
import matplotlib.pyplot as plt

graph=nx.read_edgelist("graphs_edges.txt", create_using=nx.DiGraph())
print(graph.nodes())
print(graph.edges())

nx.draw_networkx(graph, with_labels=True)
plt.show()

print(graph.number_of_nodes())
print(graph.number_of_edges())

components= list(nx.strongly_connected_components(graph))
print("no. of strongly connected components:", len(components))


