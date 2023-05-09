import pandas as pd

class Repository:
    def __init__(self):
        self.final_database_open = pd.DataFrame()
        self.final_database_numeric = pd.DataFrame()

    def add_database(self, numeric, open_df):
        self.final_database_open = pd.concat([self.final_database_open, open_df], axis=0, ignore_index=True)
        self.final_database_numeric = pd.concat([self.final_database_numeric, numeric], axis=0, ignore_index=True)

    def save_to_disk(self, file_name):
        """
        Save the final merged databases to disk.
        """
        self.final_database_open.to_csv(file_name + "_open.csv", index=False)
        self.final_database_numeric.to_csv(file_name + "_numeric.csv", index=False)

    def load_from_disk(self, file_name):
        """
        Load the final merged databases from disk.
        """
        self.final_database_open = pd.read_csv(file_name + "_open.csv")
        self.final_database_numeric = pd.read_csv(file_name + "_numeric.csv")