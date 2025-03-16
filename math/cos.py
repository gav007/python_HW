def add(a,b):
    return a+b


def sub(a,b):
    return a-b


def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        return "Division by zero"
    return a/b

def menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    return choice

def main():
    while True:
        choice = menu()
        if choice == 5:
            break
        a = int(input("Enter first number: "))  
        b = int(input("Enter second number: "))
        if choice == 1:
            print("Sum is", add(a,b))
        elif choice == 2:
            print("Difference is", sub(a,b))
        elif choice == 3:
            print("Product is", mul(a,b))
        elif choice == 4:
            print("Quotient is", div(a,b))
        else:
            print("Invalid choice")

main()
