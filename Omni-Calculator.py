import math
import statistics
import sys



def main():
    if len(sys.argv) > 1:
        cli_mode()
    else:
        interactive_mode()

def cli_mode():
    command =  sys.argv[1].lower()


    try:
        numbers = []
        for i in sys.argv[2:]:
            numbers.append(float(i))

        if not numbers:
            print("Error No usable data provided")
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
            print("Unknown command. Try '-mean', 'median' or 'mode' ")
    except ValueError:
        print("Error: CLI arguments must be numbers")

def interactive_mode():
    menu_options = {1 :"Solve Quadratic Equation (ax^2 + bx + c = 0)",
                 2:"Calculate conditional probability",
                 3:"Descriptive statistics",
                 4:"Exit" } 
    
    while(True):
        print("\n-----The Omni-Calculator version(1.2)-----\n")

        for key in menu_options:
            print(f"{key}. {menu_options[key].strip()}")
        try:
            choice = int(input("Enter your choice: "))
            if (choice == 1):
                a = getFloat("Enter the value of a: ")
                b = getFloat("Enter the value of b: ")
                c = getFloat("Enter the value of c: ")
                print(quadratic_eq(a,b,c))
            elif(choice == 2):
                while True:
                    x = getFloat("Enter the probability of A and B: ")
                    if 0 <= x <= 1:
                        y = getFloat("Enter the probability of B: ")
                        if 0< y <= 1:
                            print(con_prob(x,y))
                            break
                        else:
                            print("Invalid entry try again")
                    else:
                        print("Invalid probability entry probability must range between 0 and 1")   
            elif(choice == 3):
                stats_menu = {1: "Mean",
                              2: "Median",
                              3: "Mode",
                              4: "Exit"}
                for key in stats_menu :
                    print(f"{key}. {stats_menu[key].strip()}")
                while True:
                    try:
                        value = int(input("What would you like to calculate: "))
                        if value == 1:
                            print (f"The mean is = {calculate_mean():.2f}")
                            break
                        elif value == 2:
                            print(f"The Median is = {calculate_median():.2f}")
                            break
                        elif value == 3:
                            print(f"The mode is = {calculate_mode()} ")
                            break
                        elif value == 4:
                            break
                        else:
                            print (f"Invalid value has been input please enter an integer in the range {min(stats_menu)} and {max(stats_menu)}")
        
                    except ValueError:
                        print("Please make sure you only enter numbers ")
                        continue

                    
            elif choice == 4:
                print("Goodbye thanks for using the Omni-Calculator")
                break
            else:
                print ("\nInvalid choice try again")
        except ValueError:
            print(f"Invalid entry. Please enter an integer in range {min(menu_options)} and {max(menu_options)}")


#Function to calculate the values of x in quadratic equation            
def quadratic_eq(a,b,c):
    delta = b**2 - 4*a*c
    if(delta > 0):
        print("There are 2 roots")
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        return f"x1 = {x1:.2f},x2 = {x2:.2f}"
    
    elif(delta == 0):
        print("There is 1 root")
        x = (-b)/(2*a)
        return f"x = {x:.2f}" 
    else:
        return "There are no real roots"
# function to calculate conditional probability     
def con_prob(x,y):
    try:
        prob = x/y
        return f"probability of A given B is = {prob:.2f}"
    except ZeroDivisionError:
        pass
# function to calculate mean
def calculate_mean():
    numbers = getFloatList("Enter numbers separated by a space eg '1 2 3'")
    return statistics.mean(numbers)
# function to calculate mode
def calculate_mode():
    try:
        numbers = getFloatList("Enter numbers separated by a space eg '1 2 3'")
        return statistics.mode(numbers)
    except statistics.StatisticsError:
        print("No unique mode found")

# function to calculate median  
def calculate_median():
    numbers = getFloatList("Enter numbers separated by a space eg '1 2 3'")
    return statistics.median(numbers) 
# function to get a float input from user   
def getFloat(prompt):
    while True:
        try: 
            num = float(input(prompt))
        except ValueError:
            print("Invalid value. Try again ")
        else:
            return num
# function to turn data entered by user into a float list    
def getFloatList(prompt):
     while True:
        try:
            data = input("Enter numbers separated by a space eg '1 2 3': ")
            data = data.split()
            numbers = []
            for i in data:
                numbers.append(float(i))

            if len(numbers)==0:
                print("No number was entered try again")
                continue
               
        except ValueError:
            print("Please make sure all your values are numbers")
        else:    
            return numbers
        
if __name__ == "__main__":
    main()