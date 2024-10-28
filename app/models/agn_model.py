class AGNNode:
    def __init__(self, node_id, data, domain, node_type):
        self.node_id = node_id
        self.data = data
        self.domain = domain
        self.node_type = node_type  # Adding type for node specificity
        self.relationships = []  # To store relationships with other nodes

    def add_relationship(self, other_node_id, relation_type):
        """Adds a relationship between this node and another node."""
        self.relationships.append({"node_id": other_node_id, "relationship": relation_type})

    def to_dict(self):
        """Convert AGNNode to a dictionary format for JSON serialization, including relationships."""
        return {
            "node_id": self.node_id,
            "data": self.data,
            "domain": self.domain,
            "type": self.node_type,
            "relationships": self.relationships
        }
