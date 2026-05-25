import os
import pandas as pd

class LocalDatabase:
    def __init__(self, file_path='../data/sample_data.csv'):
        self.file_path = file_path
        self.columns = ['Asset Name', 'Type', 'Quantity', 'Buy Price', 'Current Price']
        self._ensure_db_exists()

    def _ensure_db_exists(self):
        """Creates the data directory and data file if they don't exist."""
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        if not os.path.exists(self.file_path):
            df = pd.DataFrame(columns=self.columns)
            df.to_csv(self.file_path, index=False)

    def read_all(self):
        """Reads all records from your local storage."""
        return pd.read_csv(self.file_path)

    def insert_record(self, data_dict):
        """Appends a single asset investment record to storage."""
        df = self.read_all()
        new_row = pd.DataFrame([data_dict])
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(self.file_path, index=False)
        return True
