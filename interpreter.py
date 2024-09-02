#Write a program that enables users to do math, even without knowing Python.
#Prompt the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place.
#Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

#x is an integer
#y is +, -, *, or /
#z is an integer

def main():
    expression = input("Enter an expression: ")
    x, operator, z = expression.split()
    x = float(x)
    z = float(z)
    if operator == "+":
        print(f"{x} + {z} = {x + z:.1f}")
    elif operator == "-":
        print(f"{x} - {z} = {x - z:.1f}")
    elif operator == "*":
        print(f"{x} * {z} = {x * z:.1f}")
    elif operator == "/":
        print(f"{x} / {z} = {x / z:.1f}")
    else:
        print("Invalid operator")

if __name__ == "__main__":
    main()


