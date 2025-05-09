import io

import pandas as pd
from logger import logger

def data_info_with_logger(data):
        buffer = io.StringIO()
        data.info(buf=buffer)
        logger.info(f"Data Info:\n{buffer.getvalue()}")

def data_clean_up(input_data):

    # --- Reading CSV ---
    logger.info(f"Reading CSV file -> {input_data}")
    data = pd.read_csv(input_data)
    logger.info(f"CSV read successfully. Size: {data.shape}")

    # ---  Dataframe information ---
    logger.info("Outputting information about a dataframe:")
    data_info_with_logger(data)
    # --- Splitting cpe_id ---
    logger.info("Splitting cpe_id into vendor and product...")
    cpe_parts = data['cpe_id'].str.split(":", expand=True)
    data['vendor'] = cpe_parts[3]
    data['product'] = cpe_parts[4]

    # --- Checking for missing values ---
    null_counts = data.isnull().sum()
    logger.info("Number of missing values in columns:")
    logger.info(f"\n{null_counts}")

    # --- Deleting rows with missing cpe_id ---
    logger.info("Deleting rows with missing cpe_id...")
    data.dropna(subset=['cpe_id'], inplace=True)
    logger.info(f"Rows remaining after removing empty cpe_id: {len(data)}")

    # --- Deleting rows with missing cwe_id ---
    logger.info("ВDeleting rows with missing cwe_id...")
    data.dropna(subset=['cwe_id'], inplace=True)
    logger.info(f"Rows remaining after removing empty cwe_id: {len(data)}")

    # --- Removing cpe_id column---
    logger.info("Removing cpe_id column...")
    data.drop('cpe_id', axis=1, inplace=True)

    # --- Check for duplicates---
    duplicates = data.duplicated().sum()
    logger.info(f"Number of duplicates in the table: {duplicates}")

    # --- Converting created_at and modified_at to datetime ---
    logger.info("Conversion created_at and modified_at to datetime...")
    data['created_at'] = pd.to_datetime(data['created_at'], errors='coerce')
    data['modified_at'] = pd.to_datetime(data['modified_at'], errors='coerce')

    # --- Final information about the dataframe ---
    logger.info("Updated dataframe information after cleaning:")
    data_info_with_logger(data)
    return data