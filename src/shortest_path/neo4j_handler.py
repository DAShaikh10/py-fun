"""
docker run --name neo4j-b4-graph -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=neo4j/password123 neo4j:latest
"""

from neo4j import GraphDatabase


class Neo4jHandler:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def clear_database(self):
        """
        Wipes the database clean before we start.
        """

        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")
            print("Database cleared.")

    def store_graph(self, graph_data):
        """
        Iterates through the Python Dictionary graph and stores it in Neo4j.
        Uses MERGE to ensure nodes aren't duplicated.
        """
        query = """
        MERGE (u:Node {name: $u_name})
        MERGE (v:Node {name: $v_name})
        MERGE (u)-[:CONNECTED_TO {weight: $weight}]->(v)
        """

        with self.driver.session() as session:
            count = 0
            for u_node, neighbors in graph_data.items():
                for v_node, weight in neighbors.items():
                    session.run(query, u_name=u_node, v_name=v_node, weight=weight)
                    count += 1
            print(f"Stored {count} relationships in Neo4j.")

    def fetch_graph(self):
        """
        Fetches the entire graph from Neo4j and reconstructs the
        dictionary format needed for the Dijkstra algorithm.
        """
        query = """
        MATCH (u:Node)-[r:CONNECTED_TO]->(v:Node)
        RETURN u.name as source, v.name as target, r.weight as weight
        """

        # Initialize empty graph structure
        reconstructed_graph = {}
        with self.driver.session() as session:
            result = session.run(query)
            for record in result:
                source = record["source"]
                target = record["target"]
                weight = record["weight"]

                if source not in reconstructed_graph:
                    reconstructed_graph[source] = {}
                if target not in reconstructed_graph:
                    reconstructed_graph[target] = (
                        {}
                    )  # Ensure target exists as a key too

                reconstructed_graph[source][target] = weight

        return reconstructed_graph
