from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Append paths smoothly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from portfolio import PortfolioManager
from auth import AuthManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# Core Instances
pm = PortfolioManager(csv_path='../data/sample_data.csv')
auth = AuthManager()

# ================= AUTH ENDPOINTS =================

@app.route('/api/auth/register', methods=['POST'])
def register():
    data = request.json or {}
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"error": "Username and password required."}), 400
        
    success, message = auth.register_user(username, password)
    if success:
        return jsonify({"message": message}), 201
    return jsonify({"error": message}), 400

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.json or {}
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"error": "Username and password required."}), 400
        
    success, message = auth.authenticate_user(username, password)
    if success:
        return jsonify({"message": message, "user": username}), 200
    return jsonify({"error": message}), 401

# ================= PORTFOLIO ENDPOINTS =================

@app.route('/api/portfolio', methods=['GET'])
def get_portfolio():
    try:
        summary = pm.calculate_summary()
        return jsonify(summary), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/invest', methods=['POST'])
def add_asset():
    data = request.json
    try:
        pm.add_investment(
            name=data['name'],
            asset_type=data['type'],
            quantity=data['quantity'],
            buy_price=data['buy_price'],
            current_price=data['current_price']
        )
        return jsonify({"message": "Asset added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
