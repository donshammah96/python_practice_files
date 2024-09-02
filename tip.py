def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percentage = percentage_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percentage
    print(f"Leave: ${tip:.2f}")


def dollars_to_float(d):
    return round(float(str(d).replace("$", "", 1)))


def percentage_to_float(p):
    return float(str(p).replace("%", "")) / 100

main()

