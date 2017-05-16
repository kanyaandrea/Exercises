import random


def get_random_numbers(item_qty, min_value, max_value):
    random_numbers = []
    for item in range(item_qty):
        random_numbers.append(random.randint(min_value, max_value))
    return random_numbers


def guess_game(numbers_list, max_value):
    for item in numbers_list:
        guess = int(input("Enter an integer from 1 to {}: " .format(max_value)))
        while item != guess:
            if guess < item:
                print("guess is low")
                guess = int(input("Enter an integer from 1 to {}: ".format(max_value)))
            elif guess > item:
                print("guess is high")
                guess = int(input("Enter an integer from 1 to {}: ".format(max_value)))
        print("you guessed it!")


def main():
    guess_game(get_random_numbers(2, 1, 99), 99)
    guess_game(get_random_numbers(2, 1, 49), 49)


if __name__ == '__main__':
    main()