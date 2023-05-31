def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    try:
        x = num1 / num2
        return x
    except ZeroDivisionError:
        print('You have attempted to divide by 0')

# Caculates the two number arguments, using the specified operator


def calculate(num1, num2, operator):
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return subtract(num1, num2)
    elif operator == 'X':
        return multiply(num1, num2)
    elif operator == '/':
        return divide(num1, num2)
    else:
        raise ValueError('Invalid operator, please try again')


# Function to push the calcluations to calculator.txt file
def write_to_file(num1, num2, operator, result):
    with open('calculator.txt', 'a')as f:
        f.write(f'{num1} {operator} {num2} = {result}\n')

# Function that reads/ prints the specified file


def read_equations_from_file():
    while True:
        filename = input('Enter the name of the file to read equations from: ')
        try:
            with open(filename, 'r') as f:
                equations = f.readlines()
                break
        except FileNotFoundError:
            print(
                f"Error: file '{filename}' does not exist. Try calculator.txt")
    return equations

# Captures non-numerical inputs as errors


def input_error(input_message):
    while True:
        try:
            x = float(input(input_message))
            return x
        except ValueError:
            print('Input is not a number, please enter a number')

# Main calculator function


def main():
    print("Enter '+' to add, '-' to subtract, '*' to multiply, or '/' to divide.")
    choice = input(
        "Would you like to enter an equation manually (M) or read from a file (F)? ")
    if choice.lower() == 'm':
        # Make sure user is inserting a number
        num1 = input_error("Enter the first number: ")
        operator = input("Enter an operator (+, -, *, or /): ")
        num2 = input_error("Enter the second number: ")
        while True:
            try:
                result = calculate(num1, num2, operator)
                break
            except Exception as error:
                print(error)
                operator = input("Enter an operator (+, -, *, or /): ")
        print(f"{num1} {operator} {num2} = {result}")
        with open('calculator.txt', 'a') as f:
            f.write(f"{num1} {operator} {num2} = {result}\n")
    elif choice.lower() == 'f':
        equations = read_equations_from_file()
        for equation in equations:
            equation = equation.strip()
            print(equation)

    else:
        print("Error: invalid choice. Please enter 'M' or 'F'.")


# Calls the main function for this application
if __name__ == '__main__':
    main()
