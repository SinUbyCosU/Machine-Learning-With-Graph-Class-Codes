import networkx as nx
import matplotlib.pyplot as plt
import time
graph=nx.read_edgelist("graphs_edges.txt", create_using=nx.DiGraph())
print(graph.nodes())
print(graph.edges())

nx.draw_networkx(graph, with_labels=True)
plt.show()

print(graph.number_of_nodes())
print(graph.number_of_edges())

components= list(nx.strongly_connected_components(graph))
print("no. of strongly connected components:", len(components))

components=list(nx.weakly_connected_components(graph))
print("no. of weakly connected components:", len(components))

print("connected components:", nx.number_connected_components(graph.to_undirected()))
print(nx.diameter(graph.to_undirected()))

largest_component=graph.subgraph(max(nx.strongly_connected_components(graph), key=len)).to_undirected()
print(nx.diameter(largest_component))

start=time.perf_counter()

degree=nx.degree_centrality(graph.to_undirected())
closeness=nx.closeness_centrality(graph.to_undirected())
betweeness=nx.betweenness_centrality(graph.to_undirected())
eigenvector=nx.eigenvector_centrality(graph.to_undirected())

elapsed=time.perf_counter()-start
print("Time elapsed for centrality calculations:", elapsed)

karate=nx.karate_club_graph()

non_edges=list(nx.non_edges(karate))

import matplotlib.pyplot as plt
import networkx as nx
import time

graph=nx.read_edgelist("graphs_edges.txt", create_using=nx.DiGraph())
nx.draw_networkx(graph, with_labels=True)
plt.show()

print("no. of nodes", graph.number_of_nodes())
print("no. of edges", graph.number_of_edges())
print("no of scc", len(list(nx.strongly_connected_components(graph))))
print("no of wcc",len(list(nx.weakly_connected_components(graph))))
print("Diameter:",nx.diameter(graph.to_undirected()))

n=5

adj=[
    [0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0]
]

edges=[(1,2),(1,3),(2,3),(2,4),(3,4),(3,5)]
g=nx.Graph()
g.add_edges_from(edges)
nx.draw(g, with_labels=True)
plt.show()