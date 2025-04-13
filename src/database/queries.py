from neo4j import Session

def create_lattice_node(session: Session, node_id: str, properties: dict = None) -> None:
    """
    Creates a lattice node in Neo4j with the given ID and properties.

    Args:
        session: The Neo4j session object.
        node_id: The ID of the lattice node.
        properties: A dictionary of properties to set on the node (optional).
    """
    if properties is None:
        properties = {}

    # Ensure 'id' is not in properties to avoid conflict
    if 'id' in properties:
        raise ValueError("The 'id' property should not be included in the properties dictionary. Use the node_id parameter instead.")

    property_string = ""
    for key, value in properties.items():
        property_string += f", {key}: '{value}'"  # Build the property string

    query = f"CREATE (n:LatticeNode {{id: $node_id{property_string}}})"
    try:
        session.run(query, node_id=node_id, properties=properties)
        print(f"Node with id '{node_id}' and properties {properties} created successfully.")
    except Exception as e:
        print(f"Error creating node with id '{node_id}': {e}")

# Example Usage (assuming you have a session object):
# from database.connection import DatabaseConnection
# db_connection = DatabaseConnection("bolt://192.168.56.101:7687", "neo4j", "trivir#1")
# session = db_connection.get_session()

# create_lattice_node(session, "node1", {"name": "Node One", "value": 10, "type": "example"})
# create_lattice_node(session, "node2", {"name": "Node Two", "value": 20})
# create_lattice_node(session, "node3") #no properties
# session.close()
# db_connection.close()


from neo4j import Session

def create_lattice_edge(session: Session, source_id: str, target_id: str, relationship_type: str, properties: dict = None) -> None:
    """
    Creates a lattice edge (relationship) between two LatticeNode nodes in Neo4j.

    Args:
        session: The Neo4j session object.
        source_id: The ID of the source LatticeNode.
        target_id: The ID of the target LatticeNode.
        relationship_type: The type of relationship (e.g., "BELOW", "ABOVE", "PART_OF").
        properties: A dictionary of properties to set on the relationship (optional).
    """
    if properties is None:
        properties = {}

    property_string = ""
    for key, value in properties.items():
        property_string += f", {key}: '{value}'"  # Build the property string

    query = f"""
    MATCH (a:LatticeNode {id: $source_id}), (b:LatticeNode {id: $target_id})
    CREATE (a)-[r:{relationship_type} {property_string}]->(b)
    """
    try:
        print(f"{query}")
        session.run(query, source_id=source_id, target_id=target_id, relationship_type=relationship_type, properties=properties)
        print(f"Edge of type '{relationship_type}' with properties {properties} created successfully between '{source_id}' and '{target_id}'.")
    except Exception as e:
        print(f"Error creating edge between '{source_id}' and '{target_id}': {e}")

