import random


def get_random_numbers(range_limit, min_value, max_value):
    for item in range(range_limit):
        random_numbers.append(random.randint(min_value, max_value))
    return random_numbers


def convert(number_list):
    for number in number_list:
        fahrenheit = (number * 1.8) + 32
        print("celsius: " + str(number) + " fahrenheit: " + str(fahrenheit))


def main():
    number_list = get_random_numbers(3, -30, 50)
    convert(number_list)


if __name__ == '__main__':
    main()

