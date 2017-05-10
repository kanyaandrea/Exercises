

# exercise 1.
def get_max_number(number1, number2):
    if number1 > number2:
        return number1
    return number2


# exercise 2. ver 1
def get_max_num_three(number1, number2, number3):
    max_number = number1
    if max_number < number2:
        max_number = number2
    if max_number < number3:
        max_number = number3
    return max_number


# exercise 2. ver 2
def get_max_number_three(number1, number2, number3):
    numbers = [number1, number2, number3]
    max_number = 0
    for item in numbers:
        if item > max_number:
            max_number = item
    return max_number


# exercise 3
def get_lenght(lst):
    count = 0
    for item in lst:
        count += 1
    return count


# exercise 4
def check_vowel(letter):
    if letter in ('a', 'e', 'i', 'o', 'u'):
        return True
    return False


# exercise 5
def translate(text):
    text = text.lower()
    rovarspraket = []
    for letter in text:
        if letter in ('a', 'e', 'i', 'o', 'u') or letter is " ":
            rovarspraket.append(letter)
        else:
            rovarspraket.extend((letter, "o", letter))
    return "".join(rovarspraket)

# exercise 6
def summarize(lst):
    sum_list = 0
    for item in lst:
        sum_list = sum_list + item
    return sum_list

def multiply(lst):
    multy_list = 1
    for item in lst:
        multy_list = multy_list * item
    return multy_list


# exercise 7
def reverse(string):
    new_string = string[::-1]
    return new_string


def reverse_2(string):
    return string[::-1]


def reverse_3(string):
    new_string = ""
    for letter in string[::-1]:
        new_string = str(new_string) + str(letter)
    return new_string


# exercise 8
def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False


# exercise 9
def is_member(x, lst):
    for item in lst:
        if item == x:
            return(True)
    return False


# exercise 9 with "in"
def is_member2(x, lst):
    if x in lst:
        return True
    return False


# exercise 10
def is_member_lst(lst1, lst2):
    for i in lst1:
        for j in lst2:
            if i == j:
                return(True)
    return False

# exercise 10 with "in"
def is_member_lst2(lst1, lst2):
    for i in lst1:
        for j in lst2:
            if i in lst2 or j in lst1:
                return(True)
    return False



print("exercise 1: The maximum value is: %s" % get_max_number(56, 6))  # exercise 1
print("exercise 2: The maximum value is: %s" % get_max_num_three(56, 234, 83))  # exercise 2 ver 1
print("exercise 2: The maximum value is: %s" % get_max_number_three(-35, -768, 21)) # exercise 2 ver 2
print("exercise 3: The lenght of the list is: %s" % get_lenght([12, 345, 34, 234, 34, 56, 678, 23])) # exercise 3 when the arguments is a list
print("exercise 3: The lenght of the string is: %s" % get_lenght("This is a string.")) # exercise 3 when the arguments is a string
print("exercise 4: The given arguments is a vowel: %s" % check_vowel("a"))
print("exercise 5: Translated text to rovarsparket: %s"  % translate("This is a string"))
print("exercise 6:", summarize([2, 1, 3, 2, 6]))
print("exercise 6:", multiply([2, 4, 3, 2]))
print("exercise 7:", reverse("Bad Habbit"))
print("exercise 7:", reverse_2("Bad Habbit"))
print("exercise 7:", reverse_3("Bad Habbit"))
print("exercise 8:", is_palindrome("mama"))
print("exercise 9:", is_member(2, [1, 3, 5]))
print("exercise 9:", is_member("a", ["b", "d", "a"]))
print("exercise 9:", is_member("b", [1, "b", 5]))
print("exercise 10:", is_member_lst(["b", "d", 3], [1, "k", 5]))
print("exercise 10:", is_member_lst(["b", "alma", 3], [1, "alma", 5]))


