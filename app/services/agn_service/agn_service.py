import json
import os
from app.models.agn_model import AGNNode

class AGNService:
    _node_storage = {}  # In-memory storage for nodes
    _relationships = []  # Storage for relationships
    _domains = {}

    @classmethod
    def load_graph(cls, graph_file="graphs/healthcare.json"):
        """Load nodes and relationships from a JSON file and initialize the graph structure."""
        with open(graph_file, 'r') as file:
            data = json.load(file)

            # Load domains
            cls._domains = data.get("domains", {})
            for domain_name, domain_info in cls._domains.items():
                cls._node_storage[domain_name] = AGNNode(domain_name, domain_info, domain_info.get("domain"))

            # Load entities
            entities = data.get("entities", {})
            for entity_id, entity_info in entities.items():
                domain = entity_info.get("inherits_from", "general")
                node = AGNNode(entity_id, entity_info["attributes"], domain)
                cls._node_storage[entity_id] = node

            # Load relationships
            cls._relationships = data.get("relationships", [])
            for relation in cls._relationships:
                source_id = relation["source"]
                target_id = relation["target"]
                attributes = relation.get("attributes", {})

                # Add relationship to source node if both nodes exist
                source_node = cls._node_storage.get(source_id)
                target_node = cls._node_storage.get(target_id)
                if source_node and target_node:
                    source_node.add_relationship(target_node, attributes["relationship"])

    @classmethod
    def query_node(cls, node_id):
        """Retrieve a node by ID."""
        return cls._node_storage.get(node_id)

    @classmethod
    def list_nodes(cls):
        """List all nodes in the graph."""
        return {node_id: node.to_dict() for node_id, node in cls._node_storage.items()}

    @classmethod
    def list_relationships(cls):
        """List all relationships."""
        return cls._relationships
