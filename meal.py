def main():

    time = input ("What time is it? ")
    hours = convert(time)
    if not hours:
        print("Invalid time")
        return

    if 7 <= hours <= 8:
        print(f"{time}am is beakfast time!")
    elif 12 <= hours <= 13:
        print(f"{time}pm is lunch time!")
    elif 18 <= hours <= 19:
        print(f"{time}pm is dinner time!")
    elif 20 <= hours <= 23:
        print(f"{time}pm is bed time!")

def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    if hours > 12:
        hours -= 12
    return hours

if __name__ == "__main__":
    main()