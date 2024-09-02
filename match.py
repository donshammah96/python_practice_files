name = input("What's your name? ").lower()

match name: 
    case "harry" | "hermione" | "ron":
        print(f"{name.capitalize()} is in Gryffindor")
    case "draco":
        print(f"{name.capitalize()} is in Slytherin")
    case _:
        print("Who?")