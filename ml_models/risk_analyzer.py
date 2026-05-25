import numpy as np
import pandas as pd

class RiskAnalyzer:
    def __init__(self, portfolio_manager):
        self.pm = portfolio_manager

    def analyze_portfolio_risk(self):
        """
        Calculates volatility, risk scores, and performance metrics
        for the active asset list.
        """
        summary = self.pm.calculate_summary()
        assets = summary.get('assets', [])
        
        if not assets:
            return {"risk_score": "Low (No Assets)", "sharpe_ratio": 0, "metrics": []}

        risk_metrics = []
        total_value = summary['totals']['total_current_value']
        
        # Risk profiles mapped by asset class volatility characteristics
        risk_weights = {
            'Crypto': 0.85,
            'Stock': 0.40,
            'Mutual Fund': 0.15,
            'Cash': 0.01
        }

        total_weighted_risk = 0

        for asset in assets:
            asset_type = asset['Type']
            current_val = asset['Quantity'] * asset['Current Price']
            allocation_pct = (current_val / total_value) if total_value > 0 else 0
            
            # Extract base risk multiplier
            base_risk = risk_weights.get(asset_type, 0.30)
            asset_risk_contribution = base_risk * allocation_pct
            total_weighted_risk += asset_risk_contribution

            risk_metrics.append({
                "Asset Name": asset['Asset Name'],
                "Allocation (%)": round(allocation_pct * 100, 2),
                "Volatility Factor": base_risk,
                "Risk Contribution": round(asset_risk_contribution * 100, 2)
            })

        # Determine overall score
        if total_weighted_risk < 0.15:
            rating = "Conservative (Low Risk)"
        elif total_weighted_risk < 0.45:
            rating = "Balanced (Moderate Risk)"
        else:
            rating = "Aggressive (High Risk)"

        # Calculate a simulated Sharpe Ratio: (Portfolio ROI - Risk Free Rate (4%)) / Portfolio Volatility
        portfolio_roi = summary['totals']['total_roi']
        risk_free_rate = 4.0
        sharpe = (portfolio_roi - risk_free_rate) / (total_weighted_risk * 100) if total_weighted_risk > 0 else 0

        return {
            "portfolio_risk_rating": rating,
            "overall_volatility": round(total_weighted_risk * 100, 2),
            "sharpe_ratio": round(max(0, sharpe), 2),
            "asset_breakdown": risk_metrics
        }
      
