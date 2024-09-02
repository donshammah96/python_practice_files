emoticon = "v.v"

def main():
    global emoticon
    say("Is anyone there?")
    emoticon = ":d"
    say("Oh, there you are.")


def say(phrase):
    print(phrase + " " + emoticon)


if __name__ == "__main__":
    main()