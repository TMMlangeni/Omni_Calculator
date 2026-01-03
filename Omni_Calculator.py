import math
import statistics
import sys
import csv
from datetime import datetime
import re
import os


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
        else:
            print("Unknown command. Try '-mean', '-median' or '-mode'")
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

    while True:
        print("\n-----The Omni-Calculator version(1.6)-----\n")
        for key, value in menu_options.items():
            print(f"{key}. {value}")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                op = "Quadratic Equation"
                time = datetime.now().strftime("%Y-%m-%d %H:%M")
                a = getFloat("Enter the value of a: ")
                b = getFloat("Enter the value of b: ")
                c = getFloat("Enter the value of c: ")
                print(quadratic_eq(a, b, c))
                data = f"a={a}, b={b}, c={c}"
                result = quadratic_eq(a, b, c)
                calculation_hist(time, op, data, result)
            elif choice == 2:
                # Loop for probability inputs to ensure they are valid (0-1)
                time = datetime.now().strftime("%Y-%m-%d %H:%M")
                op = "Conditional Probability"
                while True:
                    x = getFloat("Enter the probability of A and B: ")
                    if 0 <= x <= 1:
                        y = getFloat("Enter the probability of B: ")
                        if 0 < y <= 1:
                            print(
                                f"The probablility of A given B = {con_prob(x, y):.2f}"
                            )
                            data = f"{x}/{y}"
                            result = round(con_prob(x, y), 2)
                            calculation_hist(time, op, data, result)
                            break
                        else:
                            print("Invalid entry: P(B) cannot be 0 or negative.")
                    else:
                        print("Invalid entry: Probabilities must be between 0 and 1.")
            elif choice == 3:
                # Sub-menu for Stats
                stats_menu = {1: "Mean", 2: "Median", 3: "Mode", 4: "Exit"}
                while True:
                    time = datetime.now().strftime("%Y-%m-%d %H:%M")
                    for key, val in stats_menu.items():
                        print(f"{key}. {val}")

                    try:
                        value = int(input("What would you like to calculate: "))
                        if value == 1:
                            op = "Descriptive Statistics: Mean"
                            data, result = interactive_mean()
                            print(f"The mean = {result:.2f}")
                            # 2. BUG FIX: Convert the list [1.0, 2.0] into a string "1.0, 2.0"
                            # This makes the CSV much cleaner
                            temp_list =[]
                            for num in data:
                                string_num = str(num) # turning numbers in the data into a string
                                temp_list.append(string_num)
                            clean_input = ", ".join(temp_list)
                            # 3. BUG FIX: Call the function with exactly 4 arguments 
                            # (Removed the 'round(result), 2' mistake)
                            calculation_hist(time, op, clean_input, result)
                            break
                        elif value == 2:
                            op = "Descriptive Statistics: Median"
                            data, result = interactive_median()
                            print(f"The Median = {result:.2f}")
                            temp_list = []
                            for num in data:
                                string_num = str(num)
                                temp_list.append(string_num)

                            clean_input = ", ".join(temp_list)                          
                            calculation_hist(time, op, clean_input, result)
                            break
                        elif value == 3:
                            op = "Descriptive Statistics: Mode"
                            data, result = interactive_mode_stats()
                            print(f"The mode = {result}")
                            temp_list = []
                            for num in data:
                                string_num = str(num)
                                temp_list.append(string_num)

                            clean_input = ", ".join(temp_list)                              
                            calculation_hist(time, op, clean_input, result)
                            break
                        elif value == 4:
                            break
                        else:
                            print(
                                f"Invalid entry try again. Ensure you enter a value in range {min(stats_menu)} to {max(stats_menu)} "
                            )

                    except ValueError:
                        print("Please enter a valid number from the menu.")

            elif choice == 4:
                history = []
                try:
                    with open("history.csv") as file:
                        reader = csv.DictReader(file)
                        for row in reader:
                            history.append(row)  # row is already a dictionary!

                    print("\n--- Calculation History (Newest First) ---")
                    for line in sorted(
                        history, key=lambda x: x["Timestamp"], reverse=True
                    ):
                        print(
                            f"{line['Timestamp']} - {line['Operation']} - {line['Input']} : {line['Result']} \n"
                        )
                except FileNotFoundError:
                    print("No history found yet. Start calculating!")
            elif choice == 5:
                confirm = input("Delete history file? (y/n): ").lower()
                if confirm.lower() == 'y':
                    if os.path.exists("history.csv"):
                        os.remove("history.csv")
                        print("History file deleted.")
                    else:
                        print("No history file found to delete.")
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


# function to print history on history.csv file
def calculation_hist(time, op, data, result):
    # Check if the file exists before we open it
    file_exists = os.path.isfile("history.csv")
    
    with open("history.csv", "a", newline="") as file:
        fieldnames = ["Timestamp", "Operation", "Input", "Result"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # BUG FIX: If the file is new, write the header first
        if not file_exists:
            writer.writeheader()
            
        writer.writerow({
            "Timestamp": time, 
            "Operation": op, 
            "Input": data, 
            "Result": result
        })

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


# --- Interactive Wrappers (Bridge between Logic and User) ---
def interactive_mean():
    data = getFloatList("Enter numbers: ")
    return data, round(calculate_mean(data), 2)


def interactive_median():
    data = getFloatList("Enter numbers: ")
    return data, round(calculate_median(data), 2)


def interactive_mode_stats():
    data = getFloatList("Enter numbers: ")
    try:
        return data, calculate_mode(data)
    except statistics.StatisticsError:
        return data, "No unique mode"


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
