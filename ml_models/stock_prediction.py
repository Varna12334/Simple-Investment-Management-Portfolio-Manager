import numpy as np
import pandas as pd

class StockTrendPredictor:
    def __init__(self, portfolio_manager):
        self.pm = portfolio_manager

    def generate_signals(self):
        """
        Analyzes purchase price history against current value 
        using simulated EMAs to calculate MACD momentum crossovers.
        """
        summary = self.pm.calculate_summary()
        assets = summary.get('assets', [])
        
        if not assets:
            return []

        signal_report = []

        for asset in assets:
            buy_price = float(asset['Buy Price'])
            current_price = float(asset['Current Price'])
            roi = float(asset['ROI (%)'])
            
            # Establish a baseline historical price trend vector for calculations
            # Simulating a 20-day historical window ending at the current price
            historical_trend = np.linspace(buy_price, current_price, num=20)
            
            # Calculate short-term (Fast) and long-term (Slow) Exponential Moving Averages
            df_trend = pd.DataFrame({'Price': historical_trend})
            fast_ema = df_trend['Price'].ewm(span=5, adjust=False).mean().iloc[-1]
            slow_ema = df_trend['Price'].ewm(span=12, adjust=False).mean().iloc[-1]
            
            # MACD Line calculation
            macd_metric = fast_ema - slow_ema
            
            # Evaluate momentum boundaries to assign institutional trade actions
            if macd_metric > 0.5 and roi > 0:
                action_signal = "STRONG BUY (Bullish Momentum)"
                confidence_rating = "High"
            elif macd_metric < -0.5 or roi < -10:
                action_signal = "STRONG SELL (Bearish Breakdown)"
                confidence_rating = "High"
            elif fast_ema > slow_ema:
                action_signal = "ACCUMULATE / HOLD (Gradual Recovery)"
                confidence_rating = "Medium"
            else:
                action_signal = "NEUTRAL / WATCH"
                confidence_rating = "Medium"

            signal_report.append({
                "Asset Name": asset['Asset Name'],
                "Current Price": round(current_price, 2),
                "Momentum Metric": round(macd_metric, 4),
                "Algorithmic Signal": action_signal,
                "Confidence": confidence_rating
            })

        return signal_report
