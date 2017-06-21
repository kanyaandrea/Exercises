import random


def get_random_numbers():
    random_numbers = []
    for item in range(0, 10):
        random_numbers.append(random.randint(1, 99))
    return random_numbers


def get_divisible():
    random_list = get_random_numbers()
    count = 0
    for item in range(0, 10):  # this is the loop!
        if random_list[item] % 7 == 0 or random_list[item] % 5 == 0 or random_list[item] % 3 == 0:
            print(str(random_list[item]) + " is divisible by 7 or 5 or 3!")
            count += 1
    print("We found " + str(count) + " numbers divisible by 7 or 5 or 3!")


def main():
    get_divisible()

if __name__ == '__main__':
    main()

