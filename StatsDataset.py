import numpy as np
import statistics as stats
import pandas as pd


class OmniStatsClass:
    def __init__(self, data):
        self.data = np.array(data)

    def update_data(self, new_data):
        self.data = np.array(new_data)
        print("Data updated succesfully.")

    def get_mean(self):
        return np.mean(self.data)

    def get_median(self):
        return np.median(self.data)

    # since numpy does not have a designated mode function like mean and median
    def get_mode(self):
        try:
            return stats.mode(self.data)
        except stats.StatisticsError:
            return f"{self.data} No Unique mode found"

    def get_std(self):
        return np.std(self.data, ddof=1)

    def get_var(self):
        return np.var(self.data, ddof=1)

    def load_from_csv(self, filepath, column_name):

        # Loads data from a CSV file into the numpy array.

        try:
            df = pd.read_csv(filepath)
            if column_name in df.columns:
                # Convert the specific column to a numpy array
                self.data = df[column_name].to_numpy(dtype=float)
                # Remove NaN (empty) values so they don't break the math
                self.data = self.data[~np.isnan(self.data)]
                print(
                    f"Successfully loaded {len(self.data)} data points from '{column_name}'"
                )
            else:
                print(f"Error: Column '{column_name}' not found in CSV.")
        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
