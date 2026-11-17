
def ft_water_reminder():
    day_since_water = int(input("Days since last watering: "))
    if day_since_water > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")


def main():
    ft_water_reminder()

if __name__ == "__main__":
    main()