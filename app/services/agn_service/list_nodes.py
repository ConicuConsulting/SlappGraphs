# app/services/agn_service/list_nodes.py

from app.services.agn_service import _node_storage
from flask import jsonify

def list_nodes(domain=None):
    """List nodes, optionally filtered by domain."""
    if domain:
        # Filter nodes by domain
        nodes = {node_id: node.to_dict() for node_id, node in _node_storage.items() if node.domain == domain}
    else:
        # Return all nodes if no domain specified
        nodes = {node_id: node.to_dict() for node_id, node in _node_storage.items()}
    return nodes
