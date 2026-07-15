from cal_func import add, subtract
from cal_multiply import multiply
from area_of_rectangle import area_of_rectangle

def main():
    print("""Select the function from the given options:
    1. Add
    2. Subtract
    3. multiply
    4. calculate area of rectangle
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
        a = float(input("Enter the length of the rectangle: "))         
        b = float(input("Enter the width of the rectangle: "))
        result = area_of_rectangle(a, b)
        print(f"The area of the rectangle with length {a} and width {b} is: {result}") 
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":  
    main()

                   
        