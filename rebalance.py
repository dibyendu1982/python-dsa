
import pprint

def rebalance_portfolio(current_allocation, target_allocation, tolerance):
    from collections import defaultdict

    overbalanced_assets = {}
    underbalanced_assets = {}
    final_allocation = current_allocation.copy()

    # Step 1–2: Classify each asset
    for asset in current_allocation:
        current = current_allocation[asset]
        target = target_allocation[asset]
        diff = current - target

        if diff > tolerance:
            overbalanced_assets[asset] = diff
        elif diff < -tolerance:
            underbalanced_assets[asset] = -diff  # store as positive

    # Step 3: Sell overbalanced assets to bring them to target
    total_proceeds = 0.0
    for asset, excess in overbalanced_assets.items():
        amount_to_sell = excess
        final_allocation[asset] -= amount_to_sell
        total_proceeds += amount_to_sell

    # Step 4: Distribute proceeds to underbalanced assets
    # Prioritize assets farthest below their target
    sorted_under = sorted(underbalanced_assets.items(), key=lambda x: x[1], reverse=True)

    for asset, shortage in sorted_under:
        amount_to_add = min(shortage, total_proceeds)
        final_allocation[asset] += amount_to_add
        total_proceeds -= amount_to_add
        if total_proceeds <= 0:
            break

    # Step 5: Round to 1 decimal place
    return {k: round(v, 1) for k, v in final_allocation.items()}

current_allocation = {'stocks': 62.0, 'bonds': 20.0, 'cash': 18.0}
target_allocation = {'stocks': 50.0, 'bonds': 30.0, 'cash': 20.0}
tolerance = 5.0


if __name__ == "__main__":
    result = rebalance_portfolio(current_allocation, target_allocation, tolerance)
    pprint.pprint(result)


