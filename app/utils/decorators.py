from functools import wraps
from flask import request, jsonify

def require_auth(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error": "Unauthorized"}), 401
        return func(*args, **kwargs)
    return decorated_function
