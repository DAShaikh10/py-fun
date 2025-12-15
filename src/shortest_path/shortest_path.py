"""
Challenge 1: Write two properties that distinguish graphs from trees.

Here are two key properties that distinguish graphs from trees:
- Cycles: Graphs can contain cycles, whereas trees strictly contain no loops).
- Root Node: Trees have a hierarchical structure defined by a single "root" node and parent-child relationships.
             Graphs do not have a mandatory root; nodes (vertices) are generally considered equal peers in the network.

Challenge 2:
1. How can Graphs be represented in general?
Graphs are typically represented using an Adjacency Matrix (a 2D grid/array where cells represent connections)
or an Adjacency List (where each node lists its immediate neighbors).

2. How can these be implemented using Python base data structures?
- Adjacency Matrix: A "list of lists" (e.g., matrix[row][col]).
- Adjacency List: A Dictionary of Dictionaries (or Dictionary of Lists).

3. Which data structure would be efficient?
A Dictionary of Dictionaries is most efficient here as it provides O(1) (constant time) lookup speed.
"""

from utils import dijkstra, print_result


# --- Challenge 3 ---
# Representing the graph using a Dictionary of Dictionaries
nodes_video = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "S"]
challenge_4 = {node: {} for node in nodes_video}

# Edges derived from the solution path (S->B->H->G->E) and standard video examples
challenge_4["S"]["A"] = 7
challenge_4["S"]["B"] = 2
challenge_4["S"]["C"] = 3
challenge_4["A"]["B"] = 3
challenge_4["A"]["D"] = 4
challenge_4["B"]["H"] = 1
challenge_4["B"]["D"] = 4
challenge_4["H"]["F"] = 3
challenge_4["H"]["G"] = 2
challenge_4["G"]["E"] = 2
challenge_4["D"]["F"] = 5

# --- Challenge 5 ---
nodes_custom = ["A", "B", "C", "D", "E", "F"]
challenge_5 = {node: {} for node in nodes_custom}


# Helper to add edges (assuming directed based on arrow notation)
def add_edge(g, u, v, w):
    g[u][v] = w
    g[v][u] = w

add_edge(challenge_5, "A", "B", 2)
add_edge(challenge_5, "B", "E", 6)
add_edge(challenge_5, "E", "C", 9)
add_edge(challenge_5, "A", "D", 8)
add_edge(challenge_5, "B", "D", 5)
add_edge(challenge_5, "D", "E", 3)
add_edge(challenge_5, "D", "F", 2)
add_edge(challenge_5, "E", "F", 1)
add_edge(challenge_5, "F", "C", 3)

if __name__ == "__main__":
    for idx, (graph, (start, end)) in enumerate(
        zip([challenge_4, challenge_5], [("S", "E"), ("A", "C")]), start=4
    ):
        print(f"--- Challenge {idx} Output ---")
        try:
            path, dist = dijkstra(graph, start, end)
            print_result(path, dist, graph)
        except:
            print("Could not find path.")
