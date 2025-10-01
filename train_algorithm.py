import re
import requests
import json

def choose_algorithm() :
    algorithm = input("Write algorithm number(one, two, three ... etc): ")
    result = algorithms.get(algorithm, lambda: "Incorrect algorithm")()
    if result is not None:
        print(result)

def one() :
    try:
        number = int(input("Write number: "))
    except ValueError:
        return "Incorrect parameter"
    
    if number % 2 == 0:
        return "Even number"
    else:
        return "Odd number"
    
def two():

    try:
        number = int(input("Write number: "))
    except ValueError:
        return "Incorrect parameter"
    
    result = 0

    for i in range(number) :
        result += i + 1
    return result

def three():

    try:
        number = int(input("Write number: "))
    except ValueError:
        return "Incorrect parameter"
    
    if number < 0:
        return "Factorial is not defined for negative numbers"
    
    result = 1

    for i in range(1, number + 1) :
        result *= i
    return result

def four():

    string = input("Write string: ")
    return string[::-1]

def five():
    
    string = input("Write string: ").replace(" ", "").lower()
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
    
    if len(list_of_numbers) == 0:
        return "List is empty, cannot calculate average"

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
    
    if len(list_of_numbers) == 0:
        return "List is empty, cannot find maximum number"

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
        target = int(input("Write number: "))
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

def eleven():
    currency = ['USD', 'EUR']
    for currency in currency:
        currency_data = requests.get(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency}&json')
        currency_data = currency_data.json()[0]
        print("┌" + "─" * 25 + "┐")
        print(f"│ 💰 Currency: {currency_data['cc']:<10} │")
        print(f"│ 💵 Exchange: {currency_data['rate']:<10} │")
        print(f"│ 📅 Date: {currency_data['exchangedate']:<14} │")
        print("└" + "─" * 25 + "┘")
        print()

# dictionary of all algorithms
algorithms = {
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
    "eleven" : eleven,
    "11" : eleven,
}

choose_algorithm()
