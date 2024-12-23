import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def square_root(x):
    if x < 0:
        return "Error! Negative value cannot have a square root."
    return math.sqrt(x)

def power(x, y):
    return math.pow(x, y)

def logarithm(x, base=10):
    if x <= 0 or base <= 0:
        return "Error! Logarithm base or argument should be greater than zero."
    return math.log(x, base)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def factorial(x):
    if x < 0:
        return "Error! Factorial is not defined for negative numbers."
    return math.factorial(x)

def menu():
    print("\nPrathvi Ka Calculator")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Square Root (√)")
    print("6. Power (^)")
    print("7. Logarithm (log)")
    print("8. Sine (sin)")
    print("9. Cosine (cos)")
    print("10. Tangent (tan)")
    print("11. Factorial (!)")
    print("12. Exit")

def main():
    while True:
        menu()
        choice = input("Enter choice (1-12): ")

        if choice == '12':
            print("Exiting Prathvi Ka Calculator. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4', '6', '7', '8', '9', '10']:
            try:
                x = float(input("Enter first number: "))
                if choice in ['1', '2', '3', '4', '6']:
                    y = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter valid numbers.\n")
                continue
        
        if choice == '1':
            print(f"Result: {add(x, y)}\n")
        elif choice == '2':
            print(f"Result: {subtract(x, y)}\n")
        elif choice == '3':
            print(f"Result: {multiply(x, y)}\n")
        elif choice == '4':
            print(f"Result: {divide(x, y)}\n")
        elif choice == '5':
            print(f"Result: {square_root(x)}\n")
        elif choice == '6':
            print(f"Result: {power(x, y)}\n")
        elif choice == '7':
            base = input("Enter the base for the logarithm (default 10): ")
            base = float(base) if base else 10
            print(f"Result: {logarithm(x, base)}\n")
        elif choice == '8':
            print(f"Result: {sine(x)}\n")
        elif choice == '9':
            print(f"Result: {cosine(x)}\n")
        elif choice == '10':
            print(f"Result: {tangent(x)}\n")
        elif choice == '11':
            if x.is_integer() and x >= 0:
                print(f"Result: {factorial(int(x))}\n")
            else:
                print("Error! Factorial is not defined for non-integer or negative numbers.\n")
        else:
            print("Invalid choice! Please enter a valid number between 1 and 12.\n")

if __name__ == "__main__":
    main()
