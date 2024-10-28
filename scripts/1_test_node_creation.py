import requests

def print_response(response):
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Non-JSON response received:", response.text)

# Test node creation in the healthcare domain
response = requests.post("http://localhost:5000/create_node", json={
    "node_id": "patient_123",
    "data": {"name": "John Doe", "age": 45, "medical_conditions": ["hypertension", "diabetes"]},
    "domain": "healthcare"
})
print("Create Node Response:", response.json())

# Test querying in the specified domain
response = requests.get("http://localhost:5000/query", params={"node_id": "patient_123", "graph": "healthcare"})
print("Query Node in Healthcare Domain Response:", end=" ")
print_response(response)

# Test querying without specifying a domain
response = requests.get("http://localhost:5000/query", params={"node_id": "patient_123"})
print("Query Node in All Domains Response:", end=" ")
print_response(response)

# Test querying a non-existent domain
response = requests.get("http://localhost:5000/query", params={"node_id": "patient_123", "graph": "finance"})
print("Query Node in Non-existent Domain Response:", end=" ")
print_response(response)
