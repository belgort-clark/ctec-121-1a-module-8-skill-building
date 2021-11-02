# Module 8 - Skill Building Exercise No. 9 Solution
# Author: Bruce Elgort
# Date: July 22, 2017

import math


def isPrime(n):
    # if the number is 2 return True as it's a prime number
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    factor = 3
    while factor <= math.sqrt(n):
        if n % factor == 0:
            return False
        factor = factor + 2
        print(factor)
    return True


def main():
    print("Prime number tester\n")
    n = eval(input("Enter a value to test: "))
    if isPrime(n):
        print(n, "is prime.")
    else:
        print(n, "is not prime.")


if __name__ == '__main__':
    main()
