
def divisible():
    nums = list(range(10, 110, 10))
    sum_num = 0
    for item in nums:
        if item % 20 == 0:
            sum_num += item
    return sum_num


def main():
    total = divisible()
    print("Summation of number not divisible by 20 is: " + str(total))


if __name__ == '__main__':
    main()

