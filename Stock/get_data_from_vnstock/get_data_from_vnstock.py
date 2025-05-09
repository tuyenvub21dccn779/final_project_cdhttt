from vnstock import Vnstock
from .date_utils import get_start_date
from datetime import datetime, timedelta
import pandas as pd

def get_data_from_vnstock(symbol, period, interval='1D'):
    end_date = datetime.now()
#     while end_date.weekday() >= 5:  # Saturday/Sunday
#         end_date = end_date - timedelta(days=1)
    start_date = get_start_date(end_date, period)
    end_date = end_date.strftime("%Y-%m-%d")
    print(f"end_date: {end_date}, start_date: {start_date}, interval: {interval}")
    
    stock = Vnstock().stock(symbol=symbol, source='VCI')
    try:
        df = stock.quote.history(start=start_date, end=end_date, interval=interval)
        # Rename columns
        df.rename(columns={
            "time": "Date",
            "open": "Open",
            "high": "High",
            "low": "Low",
            "close": "Close",
            "volume": "Volume"
        }, inplace=True)
        # Reorder columns exactly like yfinance
        df = df[["Date", "Open", "High", "Low", "Close", "Volume"]]
        # Make sure Date is datetime
        df.sort_values("Date", inplace=True)
        df.reset_index(drop=True, inplace=True)
        df.set_index("Date", inplace=True)
        return df
    except Exception as e:
        print(f"Error getting info for {symbol}: {str(e)}")
        return None

if __name__ == '__main__':
    df = get_data_from_vnstock(symbol='VCI', period='1d', interval='1m')
    print(df.index)