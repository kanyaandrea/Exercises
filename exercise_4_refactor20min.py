def is_divisible(numbers_list, divider):
    total = 0
    for item in numbers_list:
        if item % divider == 0:
            total += item
    print("Summation of number divisible by {} is: " .format(divider) + str(total))


def is_not_divisible(numbers_list, divider):
    total = 0
    for item in numbers_list:
        if item % divider != 0:
            total += item
    print("Summation of number not divisible by {} is: " .format(divider) + str(total))


def main():
    div = is_divisible(list(range(0, 110, 10)), 20)
    not_div = is_not_divisible(list(range(0, 110, 10)), 20)


if __name__ == '__main__':
    main()
