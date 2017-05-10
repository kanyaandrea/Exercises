import random
import math


def get_user_input(range_min, range_max):
    numbers = []
    for item in range(range_min, range_max):
        user_input = int((input("Please enter a number: ")))
        numbers.append(user_input)
    return numbers


def operations(numbers_list):
    count = 0
    half_item = len(numbers_list)/2
    for item in range(round(half_item)):
        print("-" * count)
        print(str(numbers_list[count+1]/numbers_list[count]) + "\n")
        count += 1
    for item in range(round(half_item), len(numbers_list)):
        print("-" * (len(numbers_list) - count))
        print(str(numbers_list[count+1]*numbers_list[count]) + "\n")
        count += 1


def main():
    user_input_numbers = get_user_input(0, 12)
    operations(user_input_numbers)


if __name__ == '__main__':
    main()
