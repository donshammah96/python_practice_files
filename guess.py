def get_guess():
    guess = int(input("Guess the number: "))
    return guess

def main():
    guess = get_guess()
    if guess == 50:
        print("Correct!")
    else:
        print("Incorrect!")


if __name__ == "__main__":
    main()