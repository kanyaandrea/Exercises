import string


# exercise 11.
def generate_n_chars(num, char):
    string = ""
    for item in range(num):
        string = string + str(char)
    return string


# exercise 11 with multiply
def generate_n_chars2(num, char):
    string = num * str(char)
    return string


# exercise 12:
def histogram(lst):
    count = 0
    for item in lst:
        print("*" * lst[count])
        count += 1

# exercise 13: missing from the list. Is it unlucky :)?


# exercise 14:
def get_max_number(lst):
    max_number = 0
    for item in lst:
        if item > max_number:
            max_number = item
    return max_number


# exercise 15:
def get_lenght_words(lst):
    lenght = []
    for word in lst:
        lenght_word = len(word)
        lenght.append(lenght_word)
    return lenght


# exercise 15 without len:
def get_lenght_words2(lst):
    lenght = []
    for word in lst:
        char = 0
        for letter in word:
            char += 1
            lenght_word = char
        lenght.append(lenght_word)
    return lenght


# exercise 16 with len:
def find_longest_word(lst):
    max_lenght = 0
    for item in lst:
        if len(item) > max_lenght:
            max_lenght = len(item)
    return max_lenght


# exercise 16 without max and len:
def find_longest_word2(lst):
    list_lenght = []
    for item in lst:
        lenght = 0
        for letter in item:
            lenght += 1
            lenght_word = lenght
        list_lenght.append(lenght_word)
    num_lenght = list_lenght
    max_lenght = 0
    for num in num_lenght:
        if num > max_lenght:
            max_lenght = num
    return max_lenght


# exercise 17:
def filter_long_words(lst, num):
    long_words = []
    for item in lst:
        if len(item) > num:
            long_words.append(item)
    return long_words


# exercise 18:
def check_palindrome(string):
    low_string = string.lower()
    reversed_string = low_string[::-1]
    if low_string == reversed_string:
        return True
    return False


def check_palindrome2(string):
    low_string = string.lower()
    reversed_string = "".join(reversed(low_string))
    if low_string == reversed_string:
        return True
    return False


def sentence_to_string(sentence):
    # sentence = string.lower()
    string_sentence = []
    exept = [".", "?", ",", "!", " "]
    for item in sentence:
        if item not in exept:
            string_sentence.append(item)
    joined_sentence = "".join(string_sentence)
    return joined_sentence


def sentence_to_string2(sentence):
    # sentence = string.lower()
    string_sentence = []
    for item in sentence:
        if item != "." and item != "?" and item != "," and item != "!" and item != " ":
            string_sentence.append(item)
    joined_sentence = "".join(string_sentence)
    print(joined_sentence)


def check_palindrome_pharse(sentence):
    joined_sentence = sentence_to_string(sentence)
    checked = check_palindrome(joined_sentence)
    return checked


def pangram(sentence):
    characters = string.ascii_letters
    count = []
    lst = list(sentence)
    for char in characters:
        for letter in sentence:
            if char == letter:
                count += 1
        return True        
    return False



print("Result of exercise 11: " + generate_n_chars(10, "h"))
print("Result of exercise 12: ")
print(histogram([11, 3, 5, 23]))
print("Result of exercise 14: " + str(get_max_number([11, 3, 5, 23])))
print("exercise 15 (without len function): " + str(get_lenght_words2(["alma", "körte", "bogyó", "nem tudom", "mmm"])))
print("exercise 16 : " + str(find_longest_word(["alma", "körte", "bogyó", "nem tudom", "mmm"])))
print(find_longest_word2(["alma", "körte", "bogyó", "nem tudom", "mmm"]))
print(filter_long_words(["alma", "körték", "bogyó", "nem tudom", "mmm"], 6))
print(check_palindrome("gorogok"))
print(check_palindrome2("GorOg"))
print(check_palindrome_pharse("Indul a gorog aludni?"))
print(check_palindrome_pharse("Nem, nem indul a gorog aludni!"))
print(pangram("brrrrrr."))

