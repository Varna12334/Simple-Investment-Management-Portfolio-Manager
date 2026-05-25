# ... (Keep existing imports at the top)
from stock_prediction import StockTrendPredictor

# ... (Keep existing app configuration instances)
trend_predictor = StockTrendPredictor(pm)

# ================= TECH SECTOR TRADING ALERTS =================

@app.route('/api/analytics/signals', methods=['GET'])
def get_trading_signals():
    """Generates technical momentum trade indicators for current allocations."""
    try:
        alerts = trend_predictor.generate_signals()
        return jsonify({"signals": alerts}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
