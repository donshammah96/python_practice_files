def main():
    x = float(input("What is x?"))
    y = float(input("What is y?"))

    z = round(x + y)
    print(f"{z:,}")
    print("x squared is: ", square(x))

def square(x):
    return x * x

if __name__ == "__main__":
    main()