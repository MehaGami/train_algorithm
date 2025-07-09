import re

def chose_algoritm() :
    algoritm = input("Write algoritm number(one, two, three ... etc): ")
    print(algoritms.get(algoritm, lambda: "Incorrect algoritm")())

def one() :
    try:
        number = int(input("write number: "))
    except ValueError:
        return "Incorrect parameter"
    
    if number % 2 == 0:
        return "Even number"
    else:
        return "Odd number"
    
def two():

    try:
        number = int(input("write number: "))
    except ValueError:
        return "Incorrect parameter"
    
    result = 0

    for i in range(number) :
        result += i + 1
    return result

def three():

    try:
        number = int(input("write number: "))
    except ValueError:
        return "Incorrect parameter"
    
    if number < 0:
        return "Factorial is not defined for negative numbers"
    
    result = 1

    for i in range(1, number + 1) :
        result *= i
    return result

def four():

    string = input("write string: ")
    return string[::-1]

def five():
    
    string = input("write string: ").replace(" ", "").lower()
    if string == string[::-1]:
        return "Palindrome"
    else:
        return "Not a palindrome"
    
def six():
    try:
        input_numbers = input("Write numbers separated by commas: ")
        tokens = re.split(r"[,\s]+", input_numbers.strip())
        list_of_numbers = [int(x) for x in tokens if x]
    except ValueError:
        return "Incorrect parameter"
    
    result = 0

    for number in list_of_numbers:
        result += number

    return result / len(list_of_numbers)

def seven():
    try:
        input_numbers = input("Write numbers separated by commas: ")
        tokens = re.split(r"[,\s]+", input_numbers.strip())
        list_of_numbers = [int(x) for x in tokens if x]
    except ValueError:
        return "Incorrect parameter"
    
    result = list_of_numbers[0]

    for number in list_of_numbers:
        if result < number:
            result = number

    return result

def eight():
    try:
        input_numbers = input("Write numbers separated by commas: ")
        tokens = re.split(r"[,\s]+", input_numbers.strip())
        list_of_numbers = [int(x) for x in tokens if x]
    except ValueError:
        return "Incorrect parameter"
    
    try:
        target = int(input("write number: "))
    except ValueError:
        return "Incorrect parameter"
    
    count_of_target = list_of_numbers.count(target)

    return count_of_target

def nine():
    try:
        input_numbers = input("Write numbers separated by commas: ")
        tokens = re.split(r"[,\s]+", input_numbers.strip())
        list_of_numbers = [int(x) for x in tokens if x]
    except ValueError:
        return "Incorrect parameter"
    
    even_numbers_list = []
    
    for number in list_of_numbers:
        if number % 2 == 0:
            even_numbers_list.append(number)
    
    return ", ".join(map(str, even_numbers_list))

def ten():
    try:
        input_numbers = input("Write numbers separated by commas: ")
        tokens = re.split(r"[,\s]+", input_numbers.strip())
        list_of_numbers = [int(x) for x in tokens if x]
    except ValueError:
        return "Incorrect parameter"
    
    uniq_numbers_list = []
    
    for number in list_of_numbers:
        if number not in uniq_numbers_list:
            uniq_numbers_list.append(number)
    
    return ", ".join(map(str, uniq_numbers_list))

# dictionary of all algoritms
algoritms = {
    "one" : one,
    "1" : one,
    "two" : two,
    "2" : two,
    "three" : three,
    "3" : three,
    "four" : four,
    "4" : four,
    "five" : five,
    "5" : five,
    "six" : six, 
    "6" : six,
    "seven" : seven,
    "7" : seven,
    "eight" : eight,
    "8" : eight,
    "nine" : nine,
    "9" : nine,
    "ten" : ten,
    "10" : ten,
}

chose_algoritm()
