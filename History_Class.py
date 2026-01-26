import csv
import os
from Calculation_model import Calculation
from datetime import datetime
import pandas as pd


class OmniCalculator:
    def __init__(self):
        self.history_file = "history.csv"

    def log_to_csv(self, calc_obj):
        file_exists = os.path.isfile(self.history_file)
        with open(self.history_file, "a", newline="") as file:
            writer = csv.DictWriter(
                file, fieldnames=["Timestamp", "Operation", "Input", "Result"]
            )
            if not file_exists:
                writer.writeheader()

            writer.writerow(
                {
                    "Timestamp": calc_obj.time,
                    "Operation": calc_obj.operation,
                    "Input": calc_obj.input_data,
                    "Result": calc_obj.result,
                }
            )

    def view_history(self):
        history = []
        try:
            history = pd.read_csv("history.csv")
            print(history)
        except FileNotFoundError:
            print("No history found yet. Start calculating!")

    def clear_history(self):
        if os.path.exists(self.history_file):
            os.remove(self.history_file)
            print("History cleared successfully")
        else:
            print("History file already cleared.")

    # --- HERE IS THE CORRECTED FUNCTION ---
    def log_stats(self, data_array, operation, result):
        # REMOVED: calc_manager = Calculation() -> This would crash because it needs arguments.

        temp_list = []

        for num in data_array:
            string_num = str(num)
            temp_list.append(string_num)

        cleaned_input = ", ".join(temp_list)
        time = datetime.now().strftime("%Y-%m-%d %H:%M")

        # Create the object with the 4 required arguments
        current_calc = Calculation(time, operation, cleaned_input, result)

        self.log_to_csv(current_calc)
