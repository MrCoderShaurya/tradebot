import os
from binance.client import Client as BinanceClient
from binance.exceptions import BinanceAPIException, BinanceRequestException
from .logging_config import get_logger

logger = get_logger(__name__)

class BinanceFuturesClient:
    def __init__(self):
        api_key = os.environ.get("BINANCE_API_KEY")
        api_secret = os.environ.get("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise ValueError("Binance API key and secret must be set as environment variables.")

        self.client = BinanceClient(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"
        logger.info("Binance Futures client initialized for Testnet.")

    def place_order(self, order_params):
        try:
            logger.info(f"Placing order with params: {order_params}")
            order = self.client.futures_create_order(**order_params)
            logger.info(f"Order placed successfully: {order}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Binance API error: {e}")
            raise
        except BinanceRequestException as e:
            logger.error(f"Binance request error: {e}")
            raise
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            raise

