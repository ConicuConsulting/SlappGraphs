from flask import Blueprint

# Define the Blueprint
base_bp = Blueprint('base', __name__)

@base_bp.route('/')
def index():
    return "Welcome to the AGN application!"
