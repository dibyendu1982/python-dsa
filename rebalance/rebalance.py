import pprint

def rebalance_portfolio(current_allocation: dict, target_allocation: dict, tolerance: float) -> dict:
    # Return a dictionary with the rebalanced allocations, rounded to 1 decimal place.

    overbalanced_assets = {}
    underbalanced_assets = {}
    final_allocation = current_allocation.copy()
    
    # Covert the current_allocation into appropriate data type 
    current = {asset:float(value) for asset, value in current_allocation.items()}
    
    for asset in current:
        # Calcuate the difference of each asset 
        target = target_allocation[asset]
        current_val = current[asset]
        difference = current_val - target 
        # Based on the calculation add each to the overbalanced or under balanced asset 
        if difference > tolerance:
            overbalanced_assets[asset] = difference
        elif difference < -tolerance:
            underbalanced_assets[asset] = -difference # Storing as +ve as we already know that this is underbalanced asset 
        # Now we have the dictionary of the overbalanced and under balanced dictionary 
        
    # Next Step is to sell the over balanced asset to bring them to target
    # Loop through over balanced target and set the final allocation 
    total_sell_percent = 0
    for asset, excess in overbalanced_assets.items():
        percentage_to_sell = excess
        final_allocation[asset] = final_allocation[asset] - percentage_to_sell
        total_sell_percent += percentage_to_sell
        
    # Now we know the total percentage which was sold 
    # Now the time is to distribute the  total sell percentage to the largest underbalanced asset 
    # Sort the underbalanced asset dicttionary based on the value in reverse so that we have 
    sorted_underbalanced_asset = sorted(underbalanced_assets.items(), key= lambda x: x[1], reverse=True)
    
    for asset, shortage in sorted_underbalanced_asset:
        amount_to_add = min(shortage, total_sell_percent)
        final_allocation[asset] = final_allocation[asset] + amount_to_add
        total_sell_percent -= amount_to_add
        if total_sell_percent <= 0:
            break
    
    return {k:round(v,1) for k,v  in final_allocation.items()}

current_allocation = {'stocks': 62.0, 'bonds': 20.0, 'cash': 18.0}
target_allocation = {'stocks': 50.0, 'bonds': 30.0, 'cash': 20.0}
tolerance = 5.0

if __name__ == "__main__":
    result = rebalance_portfolio(current_allocation, target_allocation, tolerance)
    pprint.pprint(result)