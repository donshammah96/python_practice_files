def main():
    print_pyramid(5)


def print_column(height):
    for _ in range(height):
        print("#")

def print_pyramid(height):
    for i in range(height):
        print(" " * (height - i - 1) + "#" * (i + 1) + "  " + "#" * (i + 1) + " " * (height - i - 1))
main()