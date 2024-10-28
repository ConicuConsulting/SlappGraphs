# app/services/agn_service/load_graph.py

import json
from app.models.agn_model import AGNNode
from app.services.agn_service import _node_storage, _relationships, _domains  # Import shared globals

def load_graph(graph_file="graphs/healthcare.json"):
    """Load nodes and relationships from a JSON file and initialize the graph structure."""
    global _node_storage, _relationships, _domains

    try:
        with open(graph_file, 'r') as file:
            data = json.load(file)

            # Load domains
            _domains.clear()
            _node_storage.clear()
            _relationships.clear()

            _domains.update(data.get("domains", {}))
            print("Loading Domains...")
            for domain_name, domain_info in _domains.items():
                node_type = domain_info.get("type", "Domain")
                _node_storage[domain_name] = AGNNode(
                    node_id=domain_name,
                    data=domain_info,
                    domain=domain_info.get("domain", "general"),
                    node_type=node_type
                )
                print(f"Loaded Domain: {domain_name}, Type: {node_type}")

            # Load entities
            entities = data.get("entities", {})
            print("\nLoading Entities...")
            for entity_id, entity_info in entities.items():
                domain = entity_info.get("inherits_from", "general")
                node_type = entity_info.get("type", "Entity")
                node = AGNNode(
                    node_id=entity_id,
                    data=entity_info["attributes"],
                    domain=domain,
                    node_type=node_type
                )
                _node_storage[entity_id] = node
                print(f"Loaded Entity: {entity_id}, Domain: {domain}, Type: {node_type}")

            # Load relationships
            _relationships.extend(data.get("relationships", []))
            print("\nLoading Relationships...")
            for relation in _relationships:
                source_id = relation["source"]
                target_id = relation["target"]
                relationship_type = relation.get("attributes", {}).get("relationship", "related_to")

                source_node = _node_storage.get(source_id)
                target_node = _node_storage.get(target_id)
                
                if source_node and target_node:
                    source_node.add_relationship(target_id, relationship_type)
                    print(f"Added Relationship: {source_id} --{relationship_type}--> {target_id}")
                else:
                    print(f"Warning: Relationship skipped, missing node(s) - Source: {source_id}, Target: {target_id}")

            print("\nGraph Loaded Successfully")
            print("Total Domains:", len(_domains))
            print("Total Entities:", len(entities))
            print("Total Relationships:", len(_relationships))

    except FileNotFoundError:
        print(f"Error: File {graph_file} not found.")
    except json.JSONDecodeError:
        print("Error: Failed to parse JSON file.")

# Debug statements for immediate verification after load
print("Node Storage:", _node_storage)
print("Relationships:", _relationships)
print("Domains:", _domains)
