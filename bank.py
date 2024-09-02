#Prompt user for greeting
#If the greeting starts with “hello”, output $0
#If the greeting starts with an “h” (but not “hello”), output $20
#Otherwise output $100

greeting = input("What is your greeting? ")

if greeting.lower().startswith("hello"):
    print("$0")
elif greeting.lower().startswith("h"):
    print("$20")
else:
    print("$100")