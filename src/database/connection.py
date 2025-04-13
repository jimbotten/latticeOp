from neo4j import GraphDatabase  # Example: Neo4j

class DatabaseConnection:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def get_session(self):
        return self.driver.session()

# Example usage (in main.py or elsewhere):
# db_connection = DatabaseConnection("bolt://localhost:7687", "neo4j", "password")
# session = db_connection.get_session()
# ... use the session ...
# db_connection.close()
