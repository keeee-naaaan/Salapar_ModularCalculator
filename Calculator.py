import math

def add_numbers(num1, num2):
  """Add num1 and num2 and return the sum."""
  return num1 + num2


def subtract_numbers(num1, num2):
  """Subtract num2 from num1 and return the difference."""
  return num1 - num2


def multiply_numbers(num1, num2):
  """Multiply num1 and num2 and return the product."""
  return num1 * num2


def divide_numbers(num1, num2):
  """Divide num1 by num2 and return the quotient."""
  if num2 == 0:
    return "Error: Division by zero is not allowed."
  return num1 / num2


# Main Program Execution
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

  choice = input("Enter your choice (1/2/3/4): ")

  # 3 & 4. Call the corresponding function and store the return value
  if choice == "1":
    result = add_numbers(num1, num2)
    operation = "+"
  elif choice == "2":
    result = subtract_numbers(num1, num2)
    operation = "-"
  elif choice == "3":
    result = multiply_numbers(num1, num2)
    operation = "*"
  elif choice == "4":
    result = divide_numbers(num1, num2)
    operation = "/"
  else:
    print("Invalid choice! Please select between 1 and 4.")
    return

  # 5. Display the final answer clearly
  print("\n----------------------------------------")
  print(f"Result: {num1} {operation} {num2} = {result}")
  print("----------------------------------------")


# Run the program
if __name__ == "__main__":
  main()
