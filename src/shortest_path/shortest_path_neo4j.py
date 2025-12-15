from utils import dijkstra, print_result
from neo4j_handler import Neo4jHandler


def validate_graph(graph):
    """Ensure all nodes exist in keys for safety."""

    all_nodes = set(graph.keys())
    for neighbors in graph.values():
        all_nodes.update(neighbors.keys())
    for node in all_nodes:
        if node not in graph:
            graph[node] = {}


if __name__ == "__main__":
    # Define the Graph Data (From Challenge 4 & 5)
    graph_data_challenge_4 = {
        "A": {"B": 3, "D": 4, "S": 7},
        "B": {"A": 3, "D": 4, "H": 1, "S": 2},
        "C": {"L": 2, "S": 3},
        "D": {"A": 4, "B": 4, "F": 5},
        "E": {"G": 2, "K": 5},
        "F": {"D": 5, "H": 3},
        "G": {"E": 2, "H": 2},
        "H": {"B": 1, "F": 3, "G": 2},
        "I": {"L": 4, "J": 6, "K": 4},
        "J": {"I": 6, "L": 4, "K": 4},
        "K": {"I": 4, "J": 4, "E": 5},
        "L": {"C": 2, "I": 4, "J": 4},
        "S": {"A": 7, "B": 2, "C": 3},
    }
    graph_data_challenge_5 = {
        "A": {"B": 2, "D": 8},
        "B": {"E": 6, "D": 5},
        "D": {"E": 3, "F": 2},
        "E": {"C": 9, "F": 1},
        "F": {"C": 3},
    }

    challenges = [graph_data_challenge_4, graph_data_challenge_5]
    for graph in challenges:
        validate_graph(graph)

    db = Neo4jHandler("bolt://localhost:7687", "neo4j", "password123")
    try:
        for graph, (start, end) in zip(challenges, [("S", "E"), ("A", "C")]):
            print("--- Loading Data into Neo4j ---")
            db.clear_database()
            db.store_graph(graph)

            print("\n--- Fetching Data from Neo4j ---")
            fetched_graph = db.fetch_graph()

            print("\n--- Running Dijkstra on Fetched Graph ---")
            path, dist = dijkstra(fetched_graph, start, end)

            print_result(path, dist, fetched_graph)
    finally:
        db.close()
