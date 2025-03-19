# logger_config.py
import logging
import colorama
from log_symbols import LogSymbols

# Create a logger
logger = logging.getLogger("Signal")

LOG_STYLES = {
    "DEBUG": (colorama.Fore.LIGHTBLUE_EX, "🐛"),
    "INFO": (colorama.Fore.GREEN, "🛈"),
    "WARNING": (colorama.Fore.YELLOW, "⚠️"),
    "ERROR": (colorama.Fore.RED, "❌"),
    "CRITICAL": (
        colorama.Fore.RED + colorama.Style.BRIGHT,
        "💀",
    ),  # Custom critical symbol
}


class ColoredFormatter(logging.Formatter):
    """Custom formatter to add colors and symbols to log levels."""

    def format(self, record: logging.LogRecord):
        color, symbol = LOG_STYLES.get(record.levelname, (colorama.Style.RESET_ALL, ""))
        return f"[{colorama.Style.BRIGHT + color}{record.levelname} {record.filename}{colorama.Style.RESET_ALL}] {record.getMessage()}"


if not logger.hasHandlers():
    logger.setLevel(
        logging.DEBUG
    )  # Change this to logging.INFO or logging.WARNING in production

    # Create console handler and set level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Create formatter and add it to the handler
    formatter = ColoredFormatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
    console_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(console_handler)
