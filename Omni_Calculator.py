import math
import statistics
import sys
from datetime import datetime
import re
from Calculation_model import Calculation
from History_Class import OmniCalculator
from StatsDataset import OmniStatsClass


def main():
    # Checks if user provided command line arguments or wants the menu.
    if len(sys.argv) > 1:
        cli_mode()
    else:
        interactive_mode()


def cli_mode():
    # Handles quick calculations directly from the terminal.
    command = sys.argv[1].lower()
    try:
        # Convert all arguments after the command into a list of floats
        numbers = [float(i) for i in sys.argv[2:]]

        if not numbers:
            print("Error: No usable data provided")
            return

        if command == "-mean":
            print(f"mean: {calculate_mean(numbers):.2f}")
        elif command == "-median":
            print(f"Median: {calculate_median(numbers):.2f}")
        elif command == "-mode":
            try:
                print(f"Mode: {calculate_mode(numbers)}")
            except statistics.StatisticsError:
                print("No unique Mode found")
        elif command == "-stdev":
            print(f"Standard deviation: {calculate_std(numbers)}")
        elif command == "-variance":
            print(f"Variance: {calculate_var(numbers)}")
        else:
            print(
                "Unknown command. Try '-mean', '-median', '-mode', '-stdev', '-variance' "
            )
    except ValueError:
        print("Error: CLI arguments must be numbers")


def interactive_mode():
    # The main menu for the user interface.
    menu_options = {
        1: "Solve Quadratic Equation (ax^2 + bx + c = 0)",
        2: "Calculate conditional probability",
        3: "Descriptive statistics",
        4: "View Calculation History",
        5: "Clear Calculation History",
        6: "Exit",
    }
    calc_manager = OmniCalculator()
    print("\n-----The Omni-Calculator version(2.0)-----\n")
    while True:

        for key, value in menu_options.items():
            print(f"{key}. {value}")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                operation = "Quadratic Equation"
                time = datetime.now().strftime("%Y-%m-%d %H:%M")
                a = getFloat("Enter the value of a: ")
                b = getFloat("Enter the value of b: ")
                c = getFloat("Enter the value of c: ")
                print(f"\n{quadratic_eq(a, b, c)}\n")
                data = f"a={a}, b={b}, c={c}"
                result = quadratic_eq(a, b, c)
                current_calc = Calculation(time, operation, data, result)
                calc_manager.log_to_csv(current_calc)

            elif choice == 2:
                # Loop for probability inputs to ensure they are valid (0-1)
                time = datetime.now().strftime("%Y-%m-%d %H:%M")
                operation = "Conditional Probability"
                while True:
                    x = getFloat("Enter the probability of A and B: ")
                    if 0 <= x <= 1:
                        y = getFloat("Enter the probability of B: ")
                        if 0 < y <= 1:
                            print(
                                f"\nThe probablility of A given B = {con_prob(x, y):.2f}\n"
                            )
                            data = f"{x}/{y}"
                            result = round(con_prob(x, y), 2)
                            current_calc = Calculation(time, operation, data, result)
                            calc_manager.log_to_csv(current_calc)
                            break
                        else:
                            print("Invalid entry: P(B) cannot be 0 or negative.")
                    else:
                        print("Invalid entry: Probabilities must be between 0 and 1.")
            elif choice == 3:
                # Sub-menu for Stats

                print("\n-------Statistics Sub-Menu-------\n")

                print("1. Enter data manually")
                print("2. Load from CSV file (BIG DATA)")
                start_mode = int(input("Select option: "))

                if start_mode == 1:
                    raw_data = getFloatList("Enter data: ")
                    stats_obj = OmniStatsClass(raw_data)
                elif start_mode == 2:
                    # We create an 'empty' object first
                    stats_obj = OmniStatsClass([])

                    # Then we immediately load the file
                    filename = input("Enter (CSV) filename: ")
                    col_name = input("Enter column name: ")
                    stats_obj.load_from_csv(filename, col_name)

                else:
                    print("Invalid choice. Starting with empty dataset.")
                    stats_obj = OmniStatsClass([])

                stats_menu = {
                    1: "Mean",
                    2: "Median",
                    3: "Mode",
                    4: "Standard Deviation",
                    5: "Variance",
                    6: "Update/Change Dataset",
                    7: "Back to Main Menu",
                }

                while True:

                    for key, val in stats_menu.items():
                        print(f"{key}. {val}")
                    print("Please Enter your menu choice\n")
                    try:
                        sub_choice = int(input("What would you like to calculate: "))
                        if sub_choice == 1:
                            operation = "Descriptive Statistics: Mean"
                            result = round(stats_obj.get_mean(), 2)
                            print(f"\nThe Mean = {result}\n")
                            calc_manager.log_stats(stats_obj.data, operation, result)

                        elif sub_choice == 2:
                            operation = "Descriptive Statistics: Median"
                            result = round(stats_obj.get_median(), 2)
                            print(f"\nThe Median = {result}\n")
                            calc_manager.log_stats(stats_obj.data, operation, result)

                        elif sub_choice == 3:
                            operation = "Descriptive Statistics: Mode"
                            result = round(stats_obj.get_mode(), 2)
                            print(f"\nThe mode = {result}\n")
                            calc_manager.log_stats(stats_obj.data, operation, result)

                        elif sub_choice == 4:
                            operation = "Descriptive Statistics: Standard Deviation"
                            result = round(stats_obj.get_std(), 2)
                            print(f"\nStandard dev = {result}\n")
                            calc_manager.log_stats(stats_obj.data, operation, result)

                        elif sub_choice == 5:
                            operation = "Descriptive Statistics: Variance"
                            result = round(stats_obj.get_var(), 2)
                            print(f"\nVariance = {result}\n")
                            calc_manager.log_stats(stats_obj.data, operation, result)
                        elif sub_choice == 6:
                            print("\n---Data Update Menu---")
                            print("1. Type data manually")
                            print("2. Load from CSV file (Big Data)")
                            try:
                                update_method = int(
                                    input(
                                        "Select your preffered method of updating data: "
                                    )
                                )
                                if update_method == 1:
                                    new_data = getFloatList("Enter new data: ")
                                    stats_obj.update_data(new_data)
                                elif update_method == 2:
                                    filename = input(
                                        "Enter file name(Must be CSV file): "
                                    )
                                    colname = input("Enter Column name: ")
                                    stats_obj.load_from_csv(filename, colname)
                                else:
                                    print("Invalid entry Try again")
                            except ValueError:
                                print("Invalid Entry, Enter only integers")
                        elif sub_choice == 7:
                            confirm = input(
                                "Are you sure you want to exit? You will lose the data you've already input (y/n): "
                            )
                            if confirm.lower() == "y":
                                break
                            else:
                                continue
                        else:
                            print(
                                f"Invalid entry try again. Ensure you enter a value in range {min(stats_menu)} to {max(stats_menu)} "
                            )

                    except ValueError:
                        print("Please enter a valid number from the menu.")

            elif choice == 4:
                calc_manager.view_history()
            elif choice == 5:
                confirm = input("Delete history file? (y/n): ").lower()
                if confirm.lower() == "y":
                    calc_manager.clear_history()
                else:
                    print("Action cancelled.")
            elif choice == 6:
                print("Goodbye thanks for using the Omni-Calculator")
                break
            else:
                print(
                    f"Invalid entry try again. Ensure you enter a value in the range {min(menu_options)} to {max(menu_options)} "
                )
        except ValueError:
            print("Invalid entry. Please enter a number from the menu.")


# --- Logic Functions (Pure Functions for easy Testing) ---
def quadratic_eq(a, b, c):
    # Calculates roots for quadratic equations. Returns a formatted string.
    delta = b**2 - 4 * a * c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        # Formatted without a space after comma to match your test file assert
        return f"x1 = {x1:.2f}, x2 = {x2:.2f}"
    elif delta == 0:
        x = (-b) / (2 * a)
        return f"x = {x:.2f}"
    else:
        return "There are no real roots"


def con_prob(x, y):
    # Calculates P(A|B). Returns None if P(B) is 0.
    try:
        return x / y
    except ZeroDivisionError:
        return None


def calculate_mean(numbers):
    # Simple wrapper for statistics.mean.
    return statistics.mean(numbers)


def calculate_mode(numbers):
    # Simple wrapper for statistics.mode.

    return statistics.mode(numbers)


def calculate_median(numbers):
    # Simple wrapper for statistics.median.
    return statistics.median(numbers)


def calculate_std(numbers):
    # Simple wrapper for standard deviation
    return statistics.stdev(numbers)


def calculate_var(numbers):

    return statistics.variance(numbers)


# --- Input Helper Functions ---
def getFloat(prompt):
    # Forces user to enter a valid float.
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numerical value.")


def getFloatList(prompt):
    # Turns a space-separated string into a list of floats.
    while True:
        try:
            raw_input = input(prompt).strip()
            data = re.split(r"[,\s;]+", raw_input)
            numbers = [float(num) for num in data if num]
            if not numbers:
                print("Error: List cannot be empty.")
                continue
            return numbers
        except ValueError:
            print("Error: One or more values were not numbers.")


if __name__ == "__main__":
    main()
