from kiteconnect import KiteConnect
from config import API_KEY, ACCESS_TOKEN, CAPITAL_PER_TRADE

kite = KiteConnect(api_key=API_KEY)
kite.set_access_token(ACCESS_TOKEN)

def place_bracket_order(trading_symbol, close_price, target_pct, stop_loss_pct):
    quantity = max(1, int(CAPITAL_PER_TRADE // close_price))
    target_diff = round(close_price * target_pct / 100, 1)
    stop_loss_diff = round(close_price * stop_loss_pct / 100, 1)

    return kite.place_order(
        variety=kite.VARIETY_BO,
        exchange=kite.EXCHANGE_NSE,
        tradingsymbol=trading_symbol,
        transaction_type=kite.TRANSACTION_TYPE_BUY,
        quantity=quantity,
        order_type=kite.ORDER_TYPE_MARKET,
        product=kite.PRODUCT_MIS,
        squareoff=target_diff,
        stoploss=stop_loss_diff
    )

