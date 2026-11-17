
def ft_count_harvest_iterative():
    count = int(input("Days until harvest: "))
    for days in range(count):
        print(f"Day {days + 1}")
    print("Harvest time!")



def main():
    ft_count_harvest_iterative()

if __name__ == "__main__":
    main()