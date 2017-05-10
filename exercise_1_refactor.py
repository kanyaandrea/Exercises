import random


def guess_number(end_range, input_message):
    new_list = []
    for item in range(10):
        new_list.append(random.randint(1, end_range))
        guess = int(input(input_message))
        while new_list[item] != guess:
            if guess < new_list[item]:
                print("guess is low")
                guess = int(input(input_message))
            elif guess > new_list[item]:
                print("guess is high")
                guess = int(input(input_message))
        print("you guessed it!")


def main():
    guess_number(99, "Enter an integer from 1 to 99: ")
    guess_number(49, "Enter an integer from 1 to 49: ")

if __name__ == '__main__':
    main()

