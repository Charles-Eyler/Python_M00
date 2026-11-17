
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(f"{seed_type.capitalize()} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_type} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed_type} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")


if __name__ == "__main__":
    seed_type = input("Enter the seed type: ")
    quantity = int(input("Enter the seed quantity: "))
    unit = input("Enter the desired unit: ")
    ft_seed_inventory(seed_type, quantity, unit)
