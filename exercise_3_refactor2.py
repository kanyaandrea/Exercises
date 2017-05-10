import random
import math


def get_user_input(range_min, range_max):
    numbers = []
    for item in range(range_min, range_max):
        user_input = int((input("Please enter a number")))
        numbers.append(user_input)
    return numbers


def main():
    a = get_user_input(0, 12)
    count = 0
    half_item = len(a)/2
    for item in range(round(half_item)):
        print(" ")
        print(str(a[count+1]/a[count]) + "\n")
        count += 1
    for item in range(len(a)-round(a)):
        print("      ")
        print(str(a[count+1]*a[count]) + "\n")

if __name__ == '__main__':
    main()
