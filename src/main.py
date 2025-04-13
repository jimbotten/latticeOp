from database.connection import DatabaseConnection
from lattice.lattice_operations import add_node, add_edge

def addNodesToGraph():
    db_connection = DatabaseConnection("bolt://192.168.56.101:7687", "neo4j", "trivir#1")
    session = db_connection.get_session()

    try:
        
        add_node(session, "alice", {"name": "Alice", "age": 30})
        add_node(session, "bob", {"name": "Bob", "age": 32})
        add_node(session, "ACCOUNTS_PAYABLE", {"name": "AP"})
        add_node(session, "ACCOUNTS_RECEIVABLE", {"name": "AR"})
        add_edge(session, "alice", "ACCOUNTS_PAYABLE", "ROLE", {"weight": 1})
        add_edge(session, "alice", "ACCOUNTS_PAYABLE", "ROLE", {"weight": 1})

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()
        db_connection.close()

def main():
    print(f"Hello")    

if __name__ == "__main__":
    main()

