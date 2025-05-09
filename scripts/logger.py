import logging

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Formatter with timestamp
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# File handler
file_handler = logging.FileHandler('../process.log', mode="w")
file_handler.setFormatter(formatter)

# Add both handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
