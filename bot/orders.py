from .logging_config import get_logger

logger = get_logger(__name__)

def create_order_payload(symbol, side, order_type, quantity, price=None):
    """
    Constructs the order payload for the Binance API.
    """
    order = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
    }

    if order_type == "LIMIT":
        order["timeInForce"] = "GTC"  # Good Till Cancelled
        order["price"] = price

    logger.info(f"Created order payload: {order}")
    return order
