import pprint

def rebalance_portfolio(current_allocation: dict, target_allocation: dict, tolerance: float) -> dict:
    
    overbalanced_assets = {}
    underbalanced_assets = {}
    
    final_allocation = current_allocation.copy()
    
    # Classify each asset 
    for asset in current_allocation:
        current_value = current_allocation[asset]
        target_value = target_allocation[asset]
        difference = current_value - target_value
        
        if difference > tolerance:
            overbalanced_assets[asset] = difference
        elif difference < -tolerance:
            underbalanced_assets[asset] = -difference 
    
    # Sell the overbalanced asset 
    total_percentage_to_sell = 0.0 # Total overbalanced asset 
    for asset, excess in overbalanced_assets.items():
        percentage_to_sell = excess
        final_allocation[asset] -= percentage_to_sell
        total_percentage_to_sell += percentage_to_sell
    
    # Deal with underbalanced asset 
    # Under balanced asset is sorted from highest gap to lowest for buying 
    sorted_underbalanced_asset = sorted(underbalanced_assets.items(), key=lambda x: x[1], reverse=True)
    
    for asset, shortage in sorted_underbalanced_asset:
        amount_to_buy = min(shortage, total_percentage_to_sell)
        final_allocation[asset] += amount_to_buy
        total_percentage_to_sell -= amount_to_buy
        if amount_to_buy <= 0:
            break
        
    return {k:round(v,1) for k, v in final_allocation.items()}


current_allocation = {'stocks': 62.0, 'bonds': 20.0, 'cash': 18.0}
target_allocation = {'stocks': 50.0, 'bonds': 30.0, 'cash': 20.0}
tolerance = 5.0

if __name__ == "__main__":
    result = rebalance_portfolio(current_allocation, target_allocation, tolerance)
    pprint.pprint(result)