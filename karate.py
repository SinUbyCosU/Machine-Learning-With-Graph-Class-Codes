import matplotlib.pyplot as plt
import networkx as nx


edges=[(1,2),(1,3),(2,3),(2,4),(3,4),(3,5)]
G=nx.DiGraph()
G.add_edges_from(edges)
nx.draw(G,with_labels=True)
plt.show()

print(nx.number_of_nodes(G))
print(nx.number_of_edges(G))
print(list(G.edges()))
print(list(G.nodes()))
print(nx.in_degree_centrality(G))
print(nx.out_degree_centrality(G))
print(nx.in_degree_centrality(G)[3])
print(nx.out_degree_centrality(G)[3])
print(nx.neighbors(G,3))
print(nx.strongly_connected_components(G))
print(list(nx.weakly_connected_components(G)))
print(nx.number_connected_components(G.to_undirected()))
print(nx.diameter(G.to_undirected()))
print(G.in_degree(3))
print(G.out_degree(3))
