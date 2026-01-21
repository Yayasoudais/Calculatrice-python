def addition(a,b):
    return a+b

def multuplication(a,b):
    return a*b

def division(a,b):
    if b== 0:
        return "Erreu: division par zéro"
    return a/b


if __name__== "__main__":
    print("Addition : 5+3 = ",addition(5,3))
    print("Soustraction: 5-3 = ", addition(5,3))