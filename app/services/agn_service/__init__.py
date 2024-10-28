# app/services/agn_service/__init__.py

_node_storage = {}  # Shared in-memory storage for nodes
_relationships = []  # Shared storage for relationships
_domains = {}  # Shared storage for domains

from .load_graph import load_graph
from .query_node import query_node
from .list_nodes import list_nodes
from .list_relationships import list_relationships
