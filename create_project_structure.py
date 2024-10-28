import os

# Define the project structure
project_structure = {
    "agn_flask_app": {
        "app": {
            "__init__.py": "",
            "config.py": "",
            "routes": {
                "__init__.py": "",
                "base.py": "",
                "agn.py": ""
            },
            "services": {
                "agn_service.py": "",
                "access_control.py": ""
            },
            "models": {
                "agn_model.py": ""
            },
            "utils": {
                "helpers.py": ""
            }
        },
        "requirements.txt": "",
        "config.py": "",
        "run.py": "",
        "README.md": ""
    }
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w') as f:
                f.write(content)

# Create the project structure
create_structure('.', project_structure)