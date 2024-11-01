def add(a, b):
    pass

def subtract(a, b):
    pass

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    n1 = float(input("-> "))
    n2 = float(input("-> "))

    if choice == '1':
        print(f"= {add(n1, n2)}")
    elif choice == '2':
        print(f"= {subtract(n1, n2)}")
    elif choice == '3':
        print(f"= {multiply(n1, n2)}")
    elif choice == '4':
        print(f"= {divide(n1, n2)}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
