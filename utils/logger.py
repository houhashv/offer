import logging
import os

def setup_logger(name: str = "pricing_system", log_file: str = "log.log", level: int = logging.INFO):
    """
    Sets up a logger that writes to a file and (optionally) to console, 
    but we rely on Rich for console, so just file here or standard stream.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Check if handler already exists to avoid duplicate logs
    if not logger.handlers:
        # File Handler
        file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
        file_handler.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
    return logger

# Create a default logger instance
logger = setup_logger()
