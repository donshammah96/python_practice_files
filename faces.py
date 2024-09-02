def convert(text):
    return text.replace(":(", "🙁").replace(":)", "🙂")

def main():
    text = input("What's your current emotional state? ")
    print("My current emotional state is", convert(text))

if __name__ == "__main__":
        main()