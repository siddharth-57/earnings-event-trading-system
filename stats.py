def compute_historical_earnings_stats(df, min_events=4):
    earnings_df = df[df["Earnings_Window_Return"] != 0]

    stats = earnings_df.groupby("Stock").agg(
        total_events=("Earnings_Window_Return", "count"),
        avg_positive_return=("Earnings_Window_Return", lambda x: x[x > 0].mean()),
        win_rate=("Earnings_Window_Return", lambda x: (x > 0).mean())
    ).reset_index()

    return stats[
        (stats["total_events"] >= min_events) &
        (stats["avg_positive_return"] > 0)
    ]

