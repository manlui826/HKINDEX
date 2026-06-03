import yfinance as yf
import pandas as pd
from datetime import datetime

def get_hsi_data():
    ticker_symbol = "^HSI"
    start_date = "2025-01-02"
    
    # Get today's date format (YYYY-MM-DD)
    today_str = datetime.today().strftime('%Y-%m-%d')
    
    print(f"Fetching {ticker_symbol} data from {start_date} to {today_str}...")
    df = yf.download(ticker_symbol, start=start_date, end=today_str, interval="1d")
    
    if not df.empty:
        df.reset_index(inplace=True)
        
        # CHANGED: Added the generation date directly into the filename string
        output_file = f"hsi_historical_data_{today_str}.xlsx"
        
        df.to_excel(output_file, index=False)
        print(f"Success! Data saved to {output_file}")
    else:
        print("No data retrieved.")

if __name__ == "__main__":
    get_hsi_data()
