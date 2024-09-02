distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44,
}


def main():
    for distance in distances.values():
        for name in distances.keys():
            print(f"{name} is {distance} AU, which is {convert(distance)} meters from Earth")


def convert(au):
    return au * 149597870700


main()