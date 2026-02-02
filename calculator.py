def calculator():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter 1, 2, 3, or 4: ")

    a = float(input("Enter the first number: ")) #float allows decimal/scientific numbers
    b = float(input("Enter the second number: "))


    if choice == '1':
        result = a + b
        print("Result:" , result)

    elif choice == '2':
        result = a - b
        print("Result:", result)

    elif choice == '3':
        result = a * b
        print("Result:", result)
    
    elif choice == '4':
        if b == 0:
            print("Error: Cannot divide by zero.") # would get an undefined number if zero is input for b
        else:
            result = a / b
            print("Result:", result)

    else:
        print("Invalid input")
        

calculator()

