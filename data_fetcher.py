import yfinance as yf
import pandas as pd
from config import STOCKS

def get_stock_data():
    all_data = []

    for stock_name, ticker in STOCKS.items():
        stock = yf.Ticker(ticker)
        price_df = stock.history(period="max")

        if price_df.empty:
            continue

        price_df.reset_index(inplace=True)
        price_df["Stock"] = stock_name
        price_df["Earnings_Surprise"] = 0.0
        price_df["Earnings_Window_Return"] = 0.0

        try:
            earnings = stock.earnings_dates
            if earnings is not None and not earnings.empty:
                earnings.reset_index(inplace=True)

                for _, row in earnings.iterrows():
                    earnings_date = row["Earnings Date"].date()
                    surprise = row.get("Surprise(%)", 0.0)

                    price_df.loc[
                        price_df["Date"].dt.date == earnings_date,
                        "Earnings_Surprise"
                    ] = surprise

                    if surprise > 0:
                        idx_list = price_df.index[
                            price_df["Date"].dt.date == earnings_date
                        ]
                        if len(idx_list) == 0:
                            continue

                        idx = idx_list[0]
                        if idx >= 5 and idx + 5 < len(price_df):
                            start_price = price_df.loc[idx - 5, "Close"]
                            end_price = price_df.loc[idx + 5, "Close"]
                            window_return = ((end_price - start_price) / start_price) * 100
                            price_df.loc[idx, "Earnings_Window_Return"] = round(window_return, 2)
        except Exception:
            pass

        all_data.append(price_df)

    return pd.concat(all_data, ignore_index=True) if all_data else pd.DataFrame()

