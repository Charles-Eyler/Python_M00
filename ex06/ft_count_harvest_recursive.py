
# receive count, receive current day
# finish when current day equals count

def ft_count_harvest_recursive(max_day, current_day):
    if current_day <= max_day:
        print(f"Day {current_day}")
        ft_count_harvest_recursive(max_day, current_day + 1)
    else:
        print("Harvest time!")


if __name__ == "__main__":
    max_day = int(input("Days until harvest: "))
    ft_count_harvest_recursive(max_day, 0)
