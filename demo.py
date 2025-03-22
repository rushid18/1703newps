"""This script prompts the user for two numbers and prints their sum."""

def add_numbers(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b

def main():
    """Gets user input, calculates sum, and displays result."""
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")

if __name__ == "__main__":
    main()
