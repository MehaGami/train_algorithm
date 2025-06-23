
def chose_algoritm() :
    algoritm = input("write algoritm number(one, two, three ... etc): ")
    print(algoritms.get(algoritm, lambda: "Incorrect algoritm")())

def one() :
    try:
        number = int(input("write number: "))
    except ValueError:
        return "incorrect parameter"
    
    if number % 2 == 0:
        return "even number"
    else:
        return "odd number"

# dictionary of all algoritms
algoritms = {
    "one" : one,
}

chose_algoritm()
