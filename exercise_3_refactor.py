

def get_numbers():
    nums = []
    while len(nums) != 11:
        user_input = int((input("Please enter a number: ")))
        nums.append(user_input)
    return nums


def operations_table(lst):
    count = 0
    for item in lst:
        if count < 5:
            print(" ")
            print(str(lst[count+1]/lst[count]) + "\n")
        if count >= 5 and count < 10:
            print(" ")
            print(str(lst[count+1]*lst[count]) + "\n")
        count += 1


def main():
    number = get_numbers()
    operations_table(number)


if __name__ == '__main__':
    main()