import pandas as pd

class PortfolioOptimizer:
    def __init__(self, portfolio_manager):
        self.pm = portfolio_manager

    def generate_optimal_rebalancing(self):
        """
        Generates suggestions to rebalance current asset categories 
        toward a diversified target baseline.
        """
        summary = self.pm.calculate_summary()
        assets = summary.get('assets', [])
        
        if not assets:
            return []

        df = pd.DataFrame(assets)
        df['Current Value'] = df['Quantity'] * df['Current Price']
        total_value = df['Current Value'].sum()

        # Group actual weights by category
        grouped = df.groupby('Type')['Current Value'].sum().reset_index()
        grouped['Current Weight (%)'] = (grouped['Current Value'] / total_value) * 100

        # Targeted institutional benchmark breakdown
        target_weights = {
            'Stock': 50.0,
            'Mutual Fund': 30.0,
            'Crypto': 10.0,
            'Cash': 10.0
        }

        rebalancing_suggestions = []
        
        for asset_type, target_pct in target_weights.items():
            current_row = grouped[grouped['Type'] == asset_type]
            current_pct = current_row['Current Weight (%)'].values[0] if not current_row.empty else 0.0
            
            variance = target_pct - current_pct
            
            if variance > 5:
                action = f"UNDERWEIGHT: Allocate more capital into {asset_type} (+{abs(variance):.1f}%)"
            elif variance < -5:
                action = f"OVERWEIGHT: Consider trimming positions in {asset_type} (-{abs(variance):.1f}%)"
            else:
                action = f"OPTIMAL: Allocation matches target profile."

            rebalancing_suggestions.append({
                "Asset Type": asset_type,
                "Current Weight (%)": round(current_pct, 2),
                "Target Benchmark (%)": target_pct,
                "Action Plan": action
            })

        return rebalancing_suggestions
