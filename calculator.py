def calculator():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")

    choice = input("Enter 1 or 2: ")

    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))


    if choice == '1':
        result = a + b
        print("Result:" , result)
    elif choice == '2':
        result = a - b
        print("Result:", result)
    else: 
        print("invalid choice")

calculator()

