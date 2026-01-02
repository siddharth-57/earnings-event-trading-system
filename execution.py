from broker import place_bracket_order

def execute_trades(df):
    buy_trades = df[df["Trade_Signal"] == "BUY"]

    for _, row in buy_trades.iterrows():
        trading_symbol = row["Stock"] + "-EQ"
        place_bracket_order(
            trading_symbol,
            row["Close"],
            row["Target_Pct"],
            row["Stop_Loss_Pct"]
        )

