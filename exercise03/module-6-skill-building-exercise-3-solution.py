# Module 6 - Skill Building Exercise No. 3 Solution
# Author: Bruce Elgort
# Date: July 22, 2017

# import math library
import math

def sphereArea(radius):
    return 4 * math.pi * radius * radius


def sphereVolume(radius):
    return 4.0/3.0 * math.pi * radius**3


def main():
    print("This program computes some properties of a sphere\n")

    r = eval(input("Please enter the radius of the sphere: "))
    print("\nThe surface area is %0.2f square units." % (sphereArea(r)))
    print("The volume is %0.2f cubic units." % (sphereVolume(r)))


main()