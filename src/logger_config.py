"""
Centralized logging configuration for the TMDb pipeline.

Features:
    - Console logging
    - File logging
    - Structured timestamps
    - Log level control

"""

import logging
import os


def setup_logger(log_file: str = "logs/pipeline.log") -> logging.Logger:
    """
    Configure and return a logger instance.
    """

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("tmdb_pipeline")
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    # Formatter
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File Handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger