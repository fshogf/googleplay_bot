import pandas as pd
import logging

logger = logging.getLogger(__name__)

def read_csv_data(file_path, encoding='utf-8'):
    try:
        return pd.read_csv(file_path, encoding=encoding)
    except Exception as e:
        logger.error(f"Error reading CSV file: {e}")
        return pd.DataFrame()