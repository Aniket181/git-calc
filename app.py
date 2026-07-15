from cal_func import add, subtract

def main():
    print("""Select the function from the given options:
    1. Add
    2. Subtract
    3. multiply
    4. Divide
          """)

    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':   
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        result = add(a, b)
        print(f"The sum of {a} and {b} is: {result}")
    elif choice == '2':
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        result = subtract(a, b)
        print(f"The difference of {a} and {b} is: {result}") 
    elif choice == '3':
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        result = multiply(a, b)
        print(f"The product of {a} and {b} is: {result}") 
    elif choice == '4':
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        try:
            result = divide(a, b)
            print(f"The division of {a} by {b} is: {result}")
        except ValueError as e:
            print(e)
    else:
        print("Invalid choice. Please select a valid option.")
              
if __name__ == "__main__":
    main()