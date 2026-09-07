"""Machine Learning with Graphs assignment solution.

Run with: python code.py
"""

from __future__ import annotations

import math
import time
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


ROOT = Path(__file__).parent
EDGE_FILE = ROOT / "graphs_edges.txt"


def load_graph_from_edgelist() -> tuple[nx.Graph, nx.DiGraph]:
	"""Load the supplied edge list as both an undirected and directed graph."""
	undirected = nx.read_edgelist(EDGE_FILE, nodetype=str, create_using=nx.Graph)
	directed = nx.read_edgelist(EDGE_FILE, nodetype=str, create_using=nx.DiGraph)
	return undirected, directed


def plot_graph(graph: nx.Graph, title: str, filename: str) -> None:
	positions = nx.spring_layout(graph, seed=42)
	plt.figure(figsize=(7, 5))
	nx.draw_networkx(
		graph,
		positions,
		with_labels=True,
		node_color="#8ecae6",
		edge_color="#555555",
		arrows=graph.is_directed(),
	)
	plt.title(title)
	plt.axis("off")
	plt.tight_layout()
	plt.savefig(ROOT / filename, dpi=150)
	plt.show()


def report_graph_statistics(graph: nx.Graph) -> None:
	print("\nGraph statistics")
	print("Number of nodes:", graph.number_of_nodes())
	print("Number of edges:", graph.number_of_edges())

	components = list(nx.connected_components(graph.to_undirected()))
	print("Number of connected components:", len(components))
	largest = graph.subgraph(max(components, key=len)).to_undirected()
	print("Diameter of largest connected component:", nx.diameter(largest))


def manual_degree_centrality(graph: nx.Graph) -> dict:
	denominator = graph.number_of_nodes() - 1
	return {
		node: graph.degree(node) / denominator if denominator else 0.0
		for node in graph.nodes
	}


def manual_closeness_centrality(graph: nx.Graph) -> dict:
	scores = {}
	for node in graph:
		distances = nx.single_source_shortest_path_length(graph, node)
		total_distance = sum(distances.values())
		reachable = len(distances) - 1
		scores[node] = reachable / total_distance if total_distance else 0.0
	return scores


def manual_betweenness_centrality(graph: nx.Graph) -> dict:
	scores = {node: 0.0 for node in graph}
	nodes = list(graph)
	for source_index, source in enumerate(nodes):
		for target in nodes[source_index + 1 :]:
			shortest_paths = list(nx.all_shortest_paths(graph, source, target))
			if not shortest_paths:
				continue
			contribution = 1.0 / len(shortest_paths)
			for path in shortest_paths:
				for node in path[1:-1]:
					scores[node] += contribution

	node_count = len(nodes)
	if node_count > 2:
		scale = 2 / ((node_count - 1) * (node_count - 2))
		scores = {node: value * scale for node, value in scores.items()}
	return scores


def manual_eigenvector_centrality(graph: nx.Graph, iterations: int = 100) -> dict:
	nodes = list(graph)
	adjacency = nx.to_numpy_array(graph, nodelist=nodes)
	vector = np.ones(len(nodes)) / math.sqrt(len(nodes))
	for _ in range(iterations):
		next_vector = adjacency @ vector
		norm = np.linalg.norm(next_vector)
		if norm == 0:
			break
		vector = next_vector / norm
	return dict(zip(nodes, vector))


def benchmark_centrality(graph: nx.Graph) -> None:
	manual_functions = {
		"degree": manual_degree_centrality,
		"closeness": manual_closeness_centrality,
		"betweenness": manual_betweenness_centrality,
		"eigenvector": manual_eigenvector_centrality,
	}
	networkx_functions = {
		"degree": nx.degree_centrality,
		"closeness": nx.closeness_centrality,
		"betweenness": nx.betweenness_centrality,
		"eigenvector": nx.eigenvector_centrality,
	}

	print("\nCentrality comparison")
	for name in manual_functions:
		start = time.perf_counter()
		manual_result = manual_functions[name](graph)
		manual_time = time.perf_counter() - start

		start = time.perf_counter()
		library_result = networkx_functions[name](graph)
		library_time = time.perf_counter() - start

		print(f"\n{name.title()} centrality")
		print("Manual:", manual_result)
		print("NetworkX:", library_result)
		print(f"Manual time: {manual_time:.8f} seconds")
		print(f"NetworkX time: {library_time:.8f} seconds")


def top_katz_predictions(graph: nx.Graph, candidates: list[tuple], beta: float = 0.01) -> list[tuple]:
	nodes = list(graph)
	adjacency = nx.to_numpy_array(graph, nodelist=nodes)
	identity = np.eye(len(nodes))
	katz_matrix = np.linalg.inv(identity - beta * adjacency) - identity
	index = {node: position for position, node in enumerate(nodes)}
	scored = [
		(left, right, katz_matrix[index[left], index[right]])
		for left, right in candidates
	]
	return sorted(scored, key=lambda item: item[2], reverse=True)[:10]


def link_prediction_analysis(graph: nx.Graph) -> None:
	candidates = list(nx.non_edges(graph))
	predictors = {
		"Common Neighbors": [
			(u, v, len(list(nx.common_neighbors(graph, u, v))))
			for u, v in candidates
		],
		"Jaccard": list(nx.jaccard_coefficient(graph, candidates)),
		"Adamic-Adar": list(nx.adamic_adar_index(graph, candidates)),
		"Preferential Attachment": list(nx.preferential_attachment(graph, candidates)),
	}
	predictors["Katz"] = top_katz_predictions(graph, candidates)

	top_sets = {}
	print("\nTop ten Karate Club link predictions")
	for name, scores in predictors.items():
		top_ten = sorted(scores, key=lambda item: item[2], reverse=True)[:10]
		top_sets[name] = {tuple(sorted((u, v))) for u, v, _ in top_ten}
		print(f"\n{name}:")
		for u, v, score in top_ten:
			print(f"  ({u}, {v}) -> {score:.6f}")

	common_links = set.intersection(*top_sets.values())
	print("\nLinks common to all five predictors:", sorted(common_links))
	print("Number common to all five:", len(common_links))


def community_analysis(graph: nx.Graph) -> None:
	group_one, group_two = nx.community.kernighan_lin_bisection(graph, seed=42)
	print("\nKernighan-Lin partition")
	print("Group 1:", sorted(group_one))
	print("Group 2:", sorted(group_two))

	communities = nx.community.louvain_communities(graph, seed=42)
	modularity = nx.community.modularity(graph, communities)
	print("\nLouvain communities")
	for number, community in enumerate(communities, start=1):
		print(f"Community {number}:", sorted(community))
	print("Modularity:", modularity)

	colors = ["#219ebc" if node in group_one else "#fb8500" for node in graph]
	positions = nx.spring_layout(graph, seed=42)
	plt.figure(figsize=(8, 6))
	nx.draw_networkx(graph, positions, node_color=colors, with_labels=True)
	plt.title("Karate Club Kernighan-Lin Partition")
	plt.axis("off")
	plt.tight_layout()
	plt.savefig(ROOT / "karate_partition.png", dpi=150)
	plt.show()


def main() -> None:
	undirected, directed = load_graph_from_edgelist()
	print("Directed graph has", directed.number_of_nodes(), "nodes and", directed.number_of_edges(), "edges.")
	plot_graph(directed, "Directed graph from graphs_edges.txt", "directed_graph.png")
	report_graph_statistics(undirected)

	complete_graph = nx.complete_graph(5)
	benchmark_centrality(complete_graph)

	karate = nx.karate_club_graph()
	link_prediction_analysis(karate)
	community_analysis(karate)


if __name__ == "__main__":
	main()
