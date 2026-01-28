from .logging_config import get_logger

logger = get_logger(__name__)

def validate_order_params(symbol, side, order_type, quantity, price=None):
    """
    Validates order parameters before sending to the API.
    """
    if not symbol:
        raise ValueError("Symbol is required.")

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be 'BUY' or 'SELL'.")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be 'MARKET' or 'LIMIT'.")

    if not isinstance(quantity, (float, int)) or quantity <= 0:
        raise ValueError("Quantity must be a positive number.")

    if order_type == "LIMIT" and (not isinstance(price, (float, int)) or price <= 0):
        raise ValueError("Price is required for LIMIT orders and must be a positive number.")

    logger.info("Order parameters validated successfully.")
    return True
