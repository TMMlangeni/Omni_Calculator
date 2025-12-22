import math
import statistics
import sys

def main():
    """Checks if user provided command line arguments or wants the menu."""
    if len(sys.argv) > 1:
        cli_mode()
    else:
        interactive_mode()

def cli_mode():
    """Handles quick calculations directly from the terminal."""
    command = sys.argv[1].lower()
    try:
        # Convert all arguments after the command into a list of floats
        numbers = [float(i) for i in sys.argv[2:]]

        if not numbers:
            print("Error: No usable data provided")
            return
        
        if command == "-mean":
            print(f"mean: {statistics.mean(numbers):.2f}")
        elif command == "-median":
            print(f"Median: {statistics.median(numbers):.2f}")
        elif command == "-mode":
            try:
                print(f"Mode: {statistics.mode(numbers)}")
            except statistics.StatisticsError:
                print("No unique Mode found")
        else:
            print("Unknown command. Try '-mean', '-median' or '-mode'")
    except ValueError:
        print("Error: CLI arguments must be numbers")

def interactive_mode():
    """The main menu for the user interface."""
    menu_options = {
        1: "Solve Quadratic Equation (ax^2 + bx + c = 0)",
        2: "Calculate conditional probability",
        3: "Descriptive statistics",
        4: "Exit",
    }

    while True:
        print("\n-----The Omni-Calculator version(1.5)-----\n")
        for key, value in menu_options.items():
            print(f"{key}. {value}")
            
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                a = getFloat("Enter the value of a: ")
                b = getFloat("Enter the value of b: ")
                c = getFloat("Enter the value of c: ")
                print(quadratic_eq(a, b, c))
            elif choice == 2:
                # Loop for probability inputs to ensure they are valid (0-1)
                while True:
                    x = getFloat("Enter the probability of A and B: ")
                    if 0 <= x <= 1:
                        y = getFloat("Enter the probability of B: ")
                        if 0 < y <= 1:
                            print(f"The probablility of A given B = {con_prob(x, y):.2f}")
                            break
                        else:
                            print("Invalid entry: P(B) cannot be 0 or negative.")
                    else:
                        print("Invalid entry: Probabilities must be between 0 and 1.")
            elif choice == 3:
                # Sub-menu for Stats
                stats_menu = {1: "Mean", 2: "Median", 3: "Mode", 4: "Exit"}
                while True:
                    for key, val in stats_menu.items():
                        print(f"{key}. {val}")
                    try:
                        value = int(input("What would you like to calculate: "))
                        if value == 1:
                            print(f"The mean is = {interactive_mean():.2f}")
                            break
                        elif value == 2:
                            print(f"The Median is = {interactive_median():.2f}")
                            break
                        elif value == 3:
                            print(f"The mode is = {interactive_mode_stats()}")
                            break
                        elif value == 4:
                            break
                    except ValueError:
                        print("Please enter a valid number for the menu.")
            elif choice == 4:
                print("Goodbye thanks for using the Omni-Calculator")
                break
        except ValueError:
            print("Invalid entry. Please enter a number from the menu.")

# --- Logic Functions (Pure Functions for easy Testing) ---

def quadratic_eq(a, b, c):
    """Calculates roots for quadratic equations. Returns a formatted string."""
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
    """Calculates P(A|B). Returns None if P(B) is 0."""
    try:
        return x / y
    except ZeroDivisionError:
        return None

def calculate_mean(numbers):
    """Simple wrapper for statistics.mean."""
    return statistics.mean(numbers)

def calculate_mode(numbers):
    """Simple wrapper for statistics.mode."""
    return statistics.mode(numbers)

def calculate_median(numbers):
    """Simple wrapper for statistics.median."""
    return statistics.median(numbers)

# --- Interactive Wrappers (Bridge between Logic and User) ---
def interactive_mean():
    data = getFloatList("Enter numbers: ")
    return calculate_mean(data)

def interactive_median():
    data = getFloatList("Enter numbers: ")
    return calculate_median(data)

def interactive_mode_stats():
    data = getFloatList("Enter numbers: ")
    try:
        return calculate_mode(data)
    except statistics.StatisticsError:
        return "No unique mode"

# --- Input Helper Functions ---
def getFloat(prompt):
    """Forces user to enter a valid float."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def getFloatList(prompt):
    """Turns a space-separated string into a list of floats."""
    while True:
        try:
            data = input(prompt).split()
            numbers = [float(i) for i in data]
            if not numbers:
                print("Error: List cannot be empty.")
                continue
            return numbers
        except ValueError:
            print("Error: One or more values were not numbers.")

if __name__ == "__main__":
    main()