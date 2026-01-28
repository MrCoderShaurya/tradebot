# Python Trading Bot

This is a CLI-based Python trading bot that places orders on Binance Futures Testnet (USDT-M).

## Setup

1.  Clone the repository.
2.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Set your Binance API keys as environment variables:
    ```bash
    export BINANCE_API_KEY=your_api_key
    export BINANCE_API_SECRET=your_api_secret
    ```

## How to Run

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 30000
```

## Assumptions

- The bot uses the Binance Futures Testnet.
- API keys are provided via environment variables for security.
