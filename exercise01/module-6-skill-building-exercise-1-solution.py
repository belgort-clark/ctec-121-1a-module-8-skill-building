# Module 6 - Skill Building Exercise No. 1 Solution
# Author: Bruce Elgort
# Date: July 22, 2017

def eieio():
    # This function sends back the string "Ee-igh, Ee-igh, Oh!" to
    # the statement that called it
    return "Ee-igh, Ee-igh, Oh!"


def refrain():
    print("Old MacDonald had a farm,", eieio())


def hada(animal):
    # Note that hada() is called with animal as a parameter
    print("And on that farm he had a", animal+",", eieio())


def witha(noise):
    # Note that the witha() function is called with noise as a parameter
    noisecomma = noise + ","
    noise2 = noisecomma + " "+noise
    print("With a", noise2, "here and a", noise2, "there.")
    print("Here a", noisecomma, "there a", noisecomma, \
        "everywhere a", noise2+".")


def verse(animal, noise):
    # Note that verse() is called with two paraemters - animal and noise
    # call the refrain() function
    refrain()
    # call the hada() function with animal as a parameter
    hada(animal)
    witha(noise)
    refrain()


def main():
    # Iterate throught a list of tuples
    # See Python.org documentation for tuples
    # Tuples are like lists, but are immutable meaning their values can't change
    # Note that iterating through this gives you two variables at a time
    for a,n in [("cow","moo"), ("pig", "oink"), ("hedgehog", "Dinsdale")]:
        # call the verse function with a and n as arguments
        verse(a,n)
        print()


main()