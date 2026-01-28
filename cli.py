import argparse
import sys
from bot.client import BinanceFuturesClient
from bot.validators import validate_order_params
from bot.orders import create_order_payload
from bot.logging_config import get_logger

# It's better to initialize the logger in the main entry point.
# The logger is configured when logging_config is imported.
logger = get_logger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")
    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"], help="Order type")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Order price (required for LIMIT orders)")

    args = parser.parse_args()

    try:
        # 1. Validate inputs
        validate_order_params(args.symbol, args.side, args.type, args.quantity, args.price)

        # 2. Construct order payload
        order_payload = create_order_payload(args.symbol, args.side, args.type, args.quantity, args.price)

        # 3. Initialize client and place order
        print("Initializing Binance client...")
        client = BinanceFuturesClient()

        print("Placing order...")
        print(f"  Symbol: {args.symbol}")
        print(f"  Side: {args.side}")
        print(f"  Type: {args.type}")
        print(f"  Quantity: {args.quantity}")
        if args.type == 'LIMIT':
            print(f"  Price: {args.price}")
        
        result = client.place_order(order_payload)

        print("\n--- Order Result ---")
        print(f"  Order ID: {result.get('orderId')}")
        print(f"  Symbol: {result.get('symbol')}")
        print(f"  Status: {result.get('status')}")
        print(f"  Avg Price: {result.get('avgPrice')}")
        print("--------------------")

    except ValueError as e:
        logger.error(f"Validation error: {e}")
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        logger.error(f"An unexpected error occurred in CLI: {e}")
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
