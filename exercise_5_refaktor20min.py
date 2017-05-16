import random


def get_random(items_qty, min_value, max_value):
    numbers_list = []
    for items in range(items_qty):
        numbers_list.append(random.randint(min_value, max_value))
    return numbers_list


def calculate_fahrenheit(celsius_list):
    for item in celsius_list:
        fahrenheit = ((item * 1.8) + 32)
        print("celsius: " + str(item) + " fahrenheit: " + str("%.2f") % fahrenheit)


def main():
    celsius_list = get_random(13, -30, 50)
    calculate_fahrenheit(celsius_list)


if __name__ == '__main__':
    main()