

def count_divisible_by_20(lst):
    numbers = lst
    count = 0
    for number in numbers:
        if number % 20 == 0:
            count += number
    return count


def count_not_divisible_by_20(lst):
    numbers = lst
    count = 0
    for number in numbers:
        if number % 20 != 0:
            count += number
    return count


def main():
    lst = list(range(10, 110, 10))
    print("Summation of number divisible by 20 is: " + str(count_divisible_by_20(lst)))
    print("Summation of number not divisible by 20 is: " + str(count_not_divisible_by_20(lst)))

if __name__ == '__main__':
    main()

