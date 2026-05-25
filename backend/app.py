from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Allow importing portfolio.py from the root directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from portfolio import PortfolioManager

app = Flask(__name__)
CORS(app)  # Connects smoothly to your frontend

# Point the manager to the data folder at the root level
pm = PortfolioManager(csv_path='../data/sample_data.csv')

@app.route('/api/portfolio', methods=['GET'])
def get_portfolio():
    """Retrieves all data and calculated metrics."""
    try:
        summary = pm.calculate_summary()
        return jsonify(summary), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/invest', methods=['POST'])
def add_asset():
    """Endpoint to submit a new holding."""
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
    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
