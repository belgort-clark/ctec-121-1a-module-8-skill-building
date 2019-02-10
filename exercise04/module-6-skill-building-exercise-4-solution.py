# Module 6 - Skill Building Exercise No. 4 Solution
# Author: Bruce Elgort
# Date: July 22, 2017

def sumN(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum


def sumNCube(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i**3
    return sum


def main():
    print("This program computes the sum and sum of cubes of the first")
    print("N natural numbers.\n")

    n = eval(input("Please enter a value for N: "))
    print("The sum of the first %d natural numbers is %d" % (n,sumN(n)))
    print("The sum of the cubes of those numbers is %d" % (sumNCube(n)))


main()
