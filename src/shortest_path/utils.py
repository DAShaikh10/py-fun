import heapq


def dijkstra(graph, start, end):
    """
    Implements Dijkstra's Shortest Path Algorithm.
    Returns the shortest distance and the path as a list of nodes.
    """
    # Priority Queue to store (distance, current_node)
    # initialized with start node and distance 0
    queue = [(0, start)]

    # Dictionary to store the shortest distance to each node
    # Initialize with infinity
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    # Dictionary to store the path (predecessor of each node)
    # Used to reconstruct the path later
    previous_nodes = {node: None for node in graph}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # Stop if we reached the destination
        if current_node == end:
            break

        # If the popped node has a greater distance than what we already found, skip it
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    # Reconstruct Path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous_nodes.get(current)
    path = path[::-1]  # Reverse to get Start -> End

    return path, distances[end]


def print_result(path, distance, graph):
    """
    Prints the path, the detailed analysis of weights, and the total distance.
    """
    if not path:
        print("No path found.")
        return

    print(f"Shortest path: {' -> '.join(path)}")
    print("Analysis:")
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]

        # Look up the weight in the 'fetched_graph' dictionary
        # We use .get() just in case, but the edge should guarantee to exist
        weight = graph[u][v]

        # Print format: Node -> Node(Weight)
        print(f"{u} -> {v}({weight})")

    print(f"Shortest distance is: {distance}\n")
    print("-" * 40, "\n")
