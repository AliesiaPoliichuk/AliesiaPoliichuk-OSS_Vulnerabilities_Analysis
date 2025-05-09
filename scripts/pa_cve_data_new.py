from pathlib import Path

from data_procesing import data_clean_up
from postgres_helper import export_to_db

input_data = "resources/cve_data.csv"

if __name__ == '__main__':
    data = data_clean_up(input_data)
    export_to_db(data)
