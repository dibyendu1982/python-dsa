## Coding Assessment: Portfolio Rebalancing with Tolerance Bands

**Problem Statement**  
Implement a function `rebalance_portfolio` that adjusts a portfolio's asset allocations based on tolerance bands. The function should:
1. Identify assets exceeding their tolerance bands.
2. Sell over-weighted assets to bring them back to target.
3. Distribute proceeds to under-weighted assets, prioritizing those farthest from their target.

---

### **Input Format**
- `current_allocation`: A dictionary where keys are asset names (str) and values are current allocations (float) as percentages (e.g., `{'stocks': 57.0, 'bonds': 28.0}`).
- `target_allocation`: A dictionary with target allocations (same structure as `current_allocation`).
- `tolerance`: A float representing the absolute tolerance percentage (e.g., `5.0` means ±5%).

### **Output Format**
Return a dictionary with the rebalanced allocations, rounded to 1 decimal place.

---

### **Examples**

#### Example 1: Single Asset Breached
**Input**  
```
current_allocation = {'stocks': 57.0, 'bonds': 28.0, 'gold': 12.0, 'cash': 3.0}
target_allocation = {'stocks': 50.0, 'bonds': 30.0, 'gold': 15.0, 'cash': 5.0}
tolerance = 5.0
```


**Explanation**  
- Stocks (57%) exceed the upper tolerance band (50% + 5% = 55%).  
- Sell 7% stocks, distribute proceeds to underweight assets (gold: -3%, cash: -2%, bonds: -2%).  
- All allocations return to target.

---

#### Example 2: Multiple Assets Breached
**Input**  

```
current_allocation = {'stocks': 62.0, 'bonds': 20.0, 'cash': 18.0}
target_allocation = {'stocks': 50.0, 'bonds': 30.0, 'cash': 20.0}
tolerance = 5.0
```



**Explanation**  
- No asset exceeds the tolerance band (stocks: 50±5%, bonds: 30±5%).  
- Return the original allocations.

---

### **Steps to Solve**
1. **Identify Overweight Assets**: Check if any asset exceeds `target + tolerance` or falls below `target - tolerance`.  
2. **Calculate Sales/Purchases**: For breached assets, compute the difference needed to return to target.  
3. **Sum Proceeds**: Total proceeds from selling overweight assets.  
4. **Identify Underweight Assets**: Sort underweight assets by deviation from target (largest first).  
5. **Distribute Proceeds**: Allocate proceeds to underweight assets until funds are exhausted.

---

### **Template Code**



---

### **Notes**
- Assume the total portfolio value is 100%.  
- Round allocations to 1 decimal place.  
- If no assets breach tolerance bands, return the original allocations.
