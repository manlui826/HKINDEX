import yfinance as yf
import pandas as pd
from datetime import datetime

def get_hsi_data():
    ticker_symbol = "^HSI"
    start_date = "2025-01-02"
    end_date = datetime.today().strftime('%Y-%m-%d')
    
    print(f"Fetching {ticker_symbol} data from {start_date} to {end_date}...")
    df = yf.download(ticker_symbol, start=start_date, end=end_date, interval="1d")
    
    if not df.empty:
        df.reset_index(inplace=True)
        output_file = "hsi_historical_data.csv"
        df.to_csv(output_file, index=False)
        print(f"Success! Data saved to {output_file}")
    else:
        print("No data retrieved.")

if __name__ == "__main__":
    get_hsi_data()
