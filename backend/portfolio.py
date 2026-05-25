from database import LocalDatabase

class PortfolioManager:
    def __init__(self):
        self.db = LocalDatabase()

    def add_investment(self, name, asset_type, quantity, buy_price, current_price):
        record = {
            'Asset Name': name,
            'Type': asset_type,
            'Quantity': float(quantity),
            'Buy Price': float(buy_price),
            'Current Price': float(current_price)
        }
        return self.db.insert_record(record)

    def get_portfolio_summary(self):
        df = self.db.read_all()
        if df.empty:
            return {"assets": [], "totals": {"invested": 0, "current": 0, "pnl": 0, "roi": 0}}

        # Calculate row-level financial metrics
        df['Total Invested'] = df['Quantity'] * df['Buy Price']
        df['Current Value'] = df['Quantity'] * df['Current Price']
        df['PnL'] = df['Current Value'] - df['Total Invested']
        df['ROI (%)'] = (df['PnL'] / df['Total Invested']) * 100

        # Compute high-level global metrics
        total_invested = df['Total Invested'].sum()
        total_current = df['Current Value'].sum()
        total_pnl = total_current - total_invested
        total_roi = (total_pnl / total_invested) * 100 if total_invested > 0 else 0

        return {
            "assets": df.round(2).to_dict(orient='records'),
            "totals": {
                "invested": round(total_invested, 2),
                "current": round(total_current, 2),
                "pnl": round(total_pnl, 2),
                "roi": round(total_roi, 2)
            }
        }
