def main():
    name = input("What is your name? ").strip().title()
    hello(name)
    hello()

def hello(to="World"):
    print("Hello,",to)

if __name__ == "__main__":
    main()