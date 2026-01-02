from data_fetcher import get_stock_data
from stats import compute_historical_earnings_stats
from strategy import generate_trade_signals
from execution import execute_trades

def main():
    print("Fetching historical data...")
    df = get_stock_data()

    print("Computing earnings statistics...")
    stats = compute_historical_earnings_stats(df)

    print("Generating trade signals...")
    df = generate_trade_signals(df, stats)

    print("Executing trades...")
    execute_trades(df)

    print("Saving results...")
    df.to_csv("data/earnings_based_trades.csv", index=False)

    print("Done.")

if __name__ == "__main__":
    main()

