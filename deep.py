# Prompt user for an answer to The Great Question of Life, the Universe, and Everything
#Output Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No

answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ").lower()

if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")