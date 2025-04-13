from database.queries import create_lattice_node, create_lattice_edge

def add_node(session, node_id, properties=None):
    create_lattice_node(session, node_id, properties)

def add_edge(session, source_id, target_id, relationship_type, properties=None):
    create_lattice_edge(session, source_id, target_id, relationship_type, properties)
