import pandas as pd
from datetime import datetime

def analyze_drug_price_changes(csv_url, n, year):
    # Read the CSV file
    df = pd.read_csv(csv_url)
    
    # Convert Effective Date to datetime
    df['Effective Date'] = pd.to_datetime(df['Effective Date'])
    
    # Filter data for the specified year
    df_year = df[df['Effective Date'].dt.year == year]
    
    # Group by NDC Description and calculate price changes
    price_changes = []
    
    for drug in df_year['NDC Description'].unique():
        drug_data = df_year[df_year['NDC Description'] == drug]
        
        if len(drug_data) > 1:
            # Sort by Effective Date
            drug_data = drug_data.sort_values('Effective Date')
            
            # Calculate price change
            first_price = drug_data['NADAC Per Unit'].iloc[0]
            last_price = drug_data['NADAC Per Unit'].iloc[-1]
            price_change = last_price - first_price
            percent_change = (price_change / first_price) * 100 if first_price != 0 else 0
            
            price_changes.append({
                'Drug Name': drug,
                'First Price': first_price,
                'Last Price': last_price,
                'Price Change': price_change,
                'Percent Change': percent_change,
                'First Date': drug_data['Effective Date'].iloc[0],
                'Last Date': drug_data['Effective Date'].iloc[-1]
            })
    
    # Convert to DataFrame
    changes_df = pd.DataFrame(price_changes)
    
    # Sort by price change
    changes_df = changes_df.sort_values('Price Change', ascending=False)
    
    # Get top n increases and decreases
    top_increases = changes_df.head(n)
    top_decreases = changes_df.tail(n)
    
    # Generate report
    print(f"\nTop {n} Drug Price Increases in {year}:")
    print("=" * 80)
    for _, row in top_increases.iterrows():
        print(f"\nDrug: {row['Drug Name']}")
        print(f"Price Change: ${row['Price Change']:.2f} ({row['Percent Change']:.2f}%)")
        print(f"From: ${row['First Price']:.2f} on {row['First Date'].strftime('%Y-%m-%d')}")
        print(f"To: ${row['Last Price']:.2f} on {row['Last Date'].strftime('%Y-%m-%d')}")
    
    print(f"\nTop {n} Drug Price Decreases in {year}:")
    print("=" * 80)
    for _, row in top_decreases.iterrows():
        print(f"\nDrug: {row['Drug Name']}")
        print(f"Price Change: ${row['Price Change']:.2f} ({row['Percent Change']:.2f}%)")
        print(f"From: ${row['First Price']:.2f} on {row['First Date'].strftime('%Y-%m-%d')}")
        print(f"To: ${row['Last Price']:.2f} on {row['Last Date'].strftime('%Y-%m-%d')}")

# Example usage
csv_url = "https://download.medicaid.gov/data/nadac-national-average-drug-acquisition-cost-12-25-2024.csv"
analyze_drug_price_changes(csv_url, n=10, year=2024)
