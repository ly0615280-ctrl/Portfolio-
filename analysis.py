import pandas as pd

try:
    # 1. डेटा फ़ाइल को लोड करना (आपके फ़ाइल नाम के अनुसार)
    df = pd.read_csv('sale.csv.csv')
    print("✅ बधाई हो! डेटा सफलतापूर्वक लोड हो गया है।\n")
    
    # कॉलम के नामों को साफ़ करना (ताकि स्पेस का कोई चक्कर न रहे)
    df.columns = df.columns.str.strip()
    
    # 2. सुरक्षित तरीके से कुल बिक्री (Total Sales) निकालना
    # अगर 'Total' नाम का कॉलम नहीं है, तो यह दूसरा मिलता-जुलता कॉलम ढूंढ लेगा
    total_col = [col for col in df.columns if 'total' in col.lower() or 'income' in col.lower()]
    
    if total_col:
        total_sales = df[total_col[0]].sum()
        print(f"💰 कुल बिक्री (Total Sales): ${total_sales:,.2f}")
    else:
        print("💰 कुल बिक्री: (डेटा में बिक्री का कॉलम नहीं मिला)")
    
    # 3. पेमेंट मोड निकालना
    pay_col = [col for col in df.columns if 'payment' in col.lower()]
    if pay_col:
        top_payment = df[pay_col[0]].mode()[0]
        print(f"💳 सबसे ज़्यादा इस्तेमाल होने वाला पेमेंट मोड: {top_payment}")
        
    # 4. एक्सेल रिपोर्ट बनाना (बिना किसी रेटिंग कॉलम के झंझट के, सीधे साफ़ रिपोर्ट)
    output_file = 'Best_Sales_Report.xlsx'
    df.to_excel(output_file, index=False)
    print(f"\n📊 सफलता! '{output_file}' नाम की एक्सेल शीट आपके फोल्डर में बन गई है।")

except Exception as e:
    print(f"❌ एक छोटा एरर आया: {e}")