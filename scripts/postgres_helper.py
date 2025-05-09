import os

from sqlalchemy import create_engine
from logger import logger

DB_URL = os.getenv("DB_LINK")

def export_to_db(data):
    # Connecting to an online database with restricted access
    # so the port has been replaced with "**********"
    if DB_URL is None:
        raise Exception("Please set correct DB_LINK sys env variable")

    logger.info("Creating a database connection...")
    engine = create_engine(DB_URL)

    # --- Export to database---
    logger.info("Export data to the pa_cve_data_new table in the PostgreSQL database...")
    data.to_sql('pa_cve_data_new', engine, if_exists='replace', index=False)
    logger.info("Data successfully exported to database.")