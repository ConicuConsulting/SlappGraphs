# Active Graph Network (AGN) Web Application

This project implements an Active Graph Network (AGN) web application using Flask. The application provides an interactive API and web interface for querying and managing hierarchical, context-aware graph data.

## Project Structure


├── README.md
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── models
│   │   └── agn_model.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── agn.py
│   │   └── base.py
│   ├── services
│   │   ├── access_control.py
│   │   └── agn_service.py
│   └── utils
│       ├── decorators.py
│       └── helpers.py
├── config.py
├── create_project_structure.py
├── docs
│   └── 1_environment.md
├── requirements.txt
└── run.py

### Features
- AGN model for storing entities with context-aware relationships.
- API endpoints for managing and querying AGNs.
- Access control to regulate data access and querying permissions.
- Utilities for simplified graph interactions and data management.

## Setup
1. **Clone the Repository**  
   ```bash
   git clone <repo_url>
   cd agn-web-app
