import logging
from logging.handlers import RotatingFileHandler
import os

# Create logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        RotatingFileHandler(
            "logs/trading_bot.log", maxBytes=10485760, backupCount=5
        ),
        logging.StreamHandler(),
    ],
)

def get_logger(name):
    return logging.getLogger(name)
