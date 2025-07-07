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
}

chose_algoritm()
