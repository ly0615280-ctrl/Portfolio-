import pandas as pd

try:
    # 1. Loading the dataset
    df = pd.read_csv('sale.csv.csv')
    print("✅ Success: Data loaded successfully!\n")
    
    # Cleaning column names by stripping whitespaces
    df.columns = df.columns.str.strip()
    
    # 2. Calculating Total Sales safely
    total_col = [col for col in df.columns if 'total' in col.lower() or 'income' in col.lower()]
    
    if total_col:
        total_sales = df[total_col].sum()
        print(f"💰 Total Sales: ${total_sales:,.2f}")
    else:
        print("💰 Total Sales: (Sales column not found in data)")
    
    # 3. Finding the most popular payment method
    pay_col = [col for col in df.columns if 'payment' in col.lower()]
    if pay_col:
        top_payment = df[pay_col].mode().iloc[0]
        print(f"💳 Most Popular Payment Method: {top_payment}")
        
    # 4. Exporting the cleaned business report to Excel
    output_file = 'Best_Sales_Report.xlsx'
    df.to_excel(output_file, index=False)
    print(f"\n📊 Success! '{output_file}' has been generated in your folder.")

except Exception as e:
    print(f"❌ An error occurred: {e}")
