# Module 6 - Skill Building Exercise No. 5 Solution
# Author: Bruce Elgort
# Date: July 22, 2017

import math

def costPer(d, price):
    return float(price) / area(d)


def area(d):
    return math.pi * (0.5*d)**2


def main():
    print("Program to calculate the value of a pizza\n")

    diam = eval(input("Enter the diameter of the pizza: "))
    cost = eval(input("Enter the price of the pizza: "))

    print("\nThe pizza costs %0.4f per square unit." % (costPer(diam,cost)))


main()
