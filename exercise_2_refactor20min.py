import random


def get_random_numbers(range_limit, min_value, max_value):
    numbers = []
    for item in range(range_limit):
        numbers.append(random.randint(min_value, max_value))
    return numbers


def is_divisible(numbers_list, divide1, divide2, divide3):
    count = 0
    for item in numbers_list:
        if item % divide1 == 0 or item % divide2 == 0 or item % divide3 == 0:
            count += 1
            print(str(item) + " is divisible by" + str(divide1) + " or " + str(divide2) + " or " + str(divide3) + "!")
    print("We found " + str(count) + " numbers divisible by" + str(divide1) + " or " + str(divide2) + " or "
            + str(divide3) + "!")


def main():
    is_divisible(get_random_numbers(10, 1, 99), 7, 5, 3)

if __name__ == '__main__':
    main()
