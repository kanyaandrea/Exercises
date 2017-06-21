import random


def give_random_numbers(range_min, range_max, random_min, random_max):
    random_numbers = []
    for item in range(range_min, range_max):
        random_numbers.append(random.randint(random_min, random_max))
    return random_numbers


def guess(numbers, user_msg):
    for i in range(len(numbers)):
        user_guess = int(input(user_msg))
        while numbers[i] != user_guess:
            if user_guess < numbers[i]:
                print("guess is low")
                user_guess = int(input(user_msg))
            elif user_guess > numbers[i]:
                print("guess is high")
                user_guess = int(input(user_msg))
            else:
                break
        print("you guessed it!")


def main():
    random = give_random_numbers(0, 10, 1, 99)
    print(random)
    guess(random, "Enter an integer from 1 to 99: ")
    random2 = give_random_numbers(0, 10, 1, 49)
    print(random2)
    guess(random2, "Enter an integer from 1 to 49: ")


if __name__ == '__main__':
    main()

