import math


def get_user_input(range_min, range_max):
    numbers = []
    for item in range(range_min, range_max):
        user_input = int((input("Please enter a number: ")))
        numbers.append(user_input)
    return numbers


def operations(numbers_list):
    count = 1
    half_item = math.floor(len(numbers_list)/2)
    for item in range(half_item):
        print("-" * count)
        print(str(numbers_list[item+1]/numbers_list[item]) + "\n")
        count += 1
    for item in range(half_item, len(numbers_list)+1):
        print("-" * (len(numbers_list) - count))
        print(str(numbers_list[item+1]*numbers_list[item]) + "\n")
        count += 1


def main():
    user_input_numbers = get_user_input(0, 11)
    operations(user_input_numbers)


if __name__ == '__main__':
    main()
