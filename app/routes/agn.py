from flask import Blueprint, jsonify, request
from app.services.agn_service import load_graph, query_node, list_nodes, list_relationships
from app.models.agn_model import AGNNode

agn_bp = Blueprint('agn', __name__)

@agn_bp.route('/create_node', methods=['POST'])
def create_node():
    data = request.json
    try:
        node_id = data['node_id']
        node_data = data['data']
        domain = data['domain']
        node_type = data.get('type', 'General')

        node = AGNNode(node_id, node_data, domain, node_type)
        return jsonify({"status": f"{node_type} node created", "node": node.to_dict(), "domain": domain}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@agn_bp.route('/load_graph', methods=['POST'])
def load_graph_endpoint():
    """Endpoint to load or reload the graph structure from JSON."""
    load_graph()
    return jsonify({"status": "Graph loaded successfully"}), 200

@agn_bp.route('/list_nodes', methods=['GET'])
def list_nodes_endpoint():
    """List nodes, optionally filtered by domain."""
    nodes = list_nodes()
    return jsonify({"nodes": nodes}), 200

@agn_bp.route('/list_relationships', methods=['GET'])
def list_relationships_endpoint():
    """List all relationships in the graph."""
    relationships = list_relationships()
    return jsonify({"relationships": relationships}), 200

@agn_bp.route('/query_node', methods=['GET'])
def query_node_endpoint():
    """Retrieve a node by ID."""
    node_id = request.args.get('node_id')
    node = query_node(node_id)
    if node:
        return jsonify({"node": node.to_dict()}), 200
    return jsonify({"error": "Node not found"}), 404
