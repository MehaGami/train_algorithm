
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

# dictionary of all algoritms
algoritms = {
    "one" : one,
    "1" : one,
    "two" : two,
    "2" : two,
}

chose_algoritm()
