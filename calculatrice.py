import math

def addition(a,b):
    return a+b

def multuplication(a,b):
    return a*b

def division(a,b):
    if b== 0:
        return "Erreu: division par zéro"
    return a/b
def puissance (a,b):
    return a**b

def racine_carree(a):
    if a<0:
        return "Erreur: nombre négatif"
    return math.sqrt(a)
def modulo(a,b):
    return a%b

def factorielle(n):
    if n==0:
        return 1
    return n*factorielle(n-1)

if __name__== "__main__":
    print("Addition : 5+3 = ",addition(5,3))
    print("Soustraction: 5-3 = ", addition(5,3))