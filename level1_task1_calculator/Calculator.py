# Simple calculator program

# Add function
def add(x, y):
    return x + y

# Subtract function
def subtract(x, y):
    return x - y

# Multiply function
def multiply(x, y):
    return x * y

# Divide function
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


while True:
    print("------ Simple Calculator ------")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice, please try again.\n")
        continue
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number, please enter numeric values.\n")
        continue
    
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    
    again = input("Do you want to calculate again? (yes/no): ")
    if again.lower() != 'yes':
        break
print("Thank you for using the calculator. Goodbye!")