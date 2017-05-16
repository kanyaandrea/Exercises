import math

def get_user_input(items_qty):
    numbers_list = []
    for item in range(items_qty):
        user_input = int((input("Please enter a number: ")))
        numbers_list.append(user_input)
    return numbers_list


def operations(numbers_list):
    count = 1
    for item in range(math.floor(len(numbers_list)/2)):
        print("-" * count)
        print(str((numbers_list[item+1])/numbers_list[item]) + "\n")
        count += 1
    for item in range(math.floor(len(numbers_list)/2), len(numbers_list)+1):
        print("-" * count)
        print(str((numbers_list[item+1])*numbers_list[item]) + "\n")
        count -= 1


def main():
    operations(get_user_input(11))


if __name__ == '__main__':
    main()
