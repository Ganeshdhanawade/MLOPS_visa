import logging
import os
from pathlib import Path
from datetime import datetime

# Define the log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Get the current working directory
current_dir = Path.cwd()

# Define the logs directory name
log_dir_name = 'logs'

# Define the logs directory path
log_dir_path = current_dir / log_dir_name  # Logs directory path

# Ensure the logs directory exists
os.makedirs(log_dir_path, exist_ok=True)

# Define the full log file path
log_file_path = log_dir_path / LOG_FILE

# Configure logging
logging.basicConfig(
    filename=str(log_file_path),  # Convert Path object to string
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)
