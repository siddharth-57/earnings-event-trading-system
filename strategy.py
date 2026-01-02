def generate_trade_signals(df, stats):
    df = df.merge(stats, on="Stock", how="left")

    df["Trade_Signal"] = "NO_TRADE"
    df["Target_Pct"] = 0.0
    df["Stop_Loss_Pct"] = 0.0

    condition = (
        (df["Earnings_Surprise"] > 0) &
        (df["avg_positive_return"].notna())
    )

    df.loc[condition, "Trade_Signal"] = "BUY"
    df.loc[condition, "Target_Pct"] = df.loc[condition, "avg_positive_return"]
    df.loc[condition, "Stop_Loss_Pct"] = 0.5 * df.loc[condition, "Target_Pct"]

    return df

