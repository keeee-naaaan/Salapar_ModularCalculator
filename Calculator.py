import math

def add_numbers(num1, num2):
    return num1 + num2


def subtract_numbers(num1, num2):
    return num1 - num2


def multiply_numbers(num1, num2):
    return num1 * num2


def divide_numbers(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2


def main():
    print("=== Calculator Program ===")

    # 1. Ask the user to enter two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # 2. Ask the user to choose an operation
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter your choice (1-4): ")

    # 3 & 4. Call the corresponding function, pass parameters, and store the return value
    if choice == "1":
        result = add_numbers(num1, num2)
        operation_symbol = "+"
    elif choice == "2":
        result = subtract_numbers(num1, num2)
        operation_symbol = "-"
    elif choice == "3":
        result = multiply_numbers(num1, num2)
        operation_symbol = "*"
    elif choice == "4":
        result = divide_numbers(num1, num2)
        operation_symbol = "/"
    else:
        result = "Invalid choice!"
        operation_symbol = "?"

    # 5. Display the final answer clearly
    if operation_symbol != "?":
        print(f"\nFinal Answer: {num1} {operation_symbol} {num2} = {result}")
    else:
        print(f"\n{result}")


# Run the program
if __name__ == "__main__":
    main()
