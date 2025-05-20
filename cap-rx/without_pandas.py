from collections import defaultdict
from datetime import datetime
import csv
from typing import List, Tuple, Dict

def parse_date(date_str: str) -> datetime:
    """Convert date string to datetime object"""
    return datetime.strptime(date_str, '%m/%d/%Y')

def get_price_changes(file_path: str, year: int, n: int = 10) -> Tuple[List[Tuple], List[Tuple]]:
    """
    Analyze price changes for drugs in a given year
    Returns top n price increases and decreases
    """
    # Dictionary to store first and last prices for each drug in the year
    drug_prices = defaultdict(lambda: {'first': None, 'last': None})
    
    # Read and process the CSV file
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                # Parse the effective date
                effective_date = parse_date(row['Effective Date'])
                
                # Only process records from the specified year
                if effective_date.year != year:
                    continue
                
                drug_name = row['NDC Description']
                price = float(row['NADAC Per Unit'])
                
                # Update first and last prices for the drug
                if drug_prices[drug_name]['first'] is None:
                    drug_prices[drug_name]['first'] = price
                drug_prices[drug_name]['last'] = price
                
            except (ValueError, KeyError) as e:
                print(f"Error processing row: {e}")
                continue
    
    # Calculate price changes
    price_changes = []
    for drug, prices in drug_prices.items():
        if prices['first'] is not None and prices['last'] is not None:
            change = prices['last'] - prices['first']
            percentage_change = (change / prices['first']) * 100 if prices['first'] != 0 else 0
            price_changes.append((drug, change, percentage_change))
    
    # Sort by percentage change
    price_changes.sort(key=lambda x: x[2])
    
    # Get top n decreases and increases
    top_decreases = price_changes[:n]
    top_increases = price_changes[-n:][::-1]  # Reverse to get highest first
    
    return top_increases, top_decreases

def generate_report(file_path: str, year: int, n: int = 10) -> None:
    """Generate and print the price change report"""
    top_increases, top_decreases = get_price_changes(file_path, year, n)
    
    print(f"\nPrice Change Report for {year}")
    print("=" * 80)
    
    print("\nTop {} Price Increases:".format(n))
    print("-" * 80)
    print(f"{'Drug Name':<50} {'Price Change':<15} {'% Change':<10}")
    print("-" * 80)
    for drug, change, pct_change in top_increases:
        print(f"{drug[:50]:<50} ${change:,.2f} {pct_change:,.2f}%")
    
    print("\nTop {} Price Decreases:".format(n))
    print("-" * 80)
    print(f"{'Drug Name':<50} {'Price Change':<15} {'% Change':<10}")
    print("-" * 80)
    for drug, change, pct_change in top_decreases:
        print(f"{drug[:50]:<50} ${change:,.2f} {pct_change:,.2f}%")

# Example usage
if __name__ == "__main__":
    file_path = "nadac-national-average-drug-acquisition-cost-12-25-2024.csv"
    year = 2024
    n = 10
    
    generate_report(file_path, year, n)
