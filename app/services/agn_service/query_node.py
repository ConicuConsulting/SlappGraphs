from .load_graph import _node_storage

def query_node(node_id):
    """Retrieve a node by ID."""
    return _node_storage.get(node_id)
