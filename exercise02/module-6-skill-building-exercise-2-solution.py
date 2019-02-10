# Module 6 - Skill Building Exercise No. 2 Solution
# Author: Bruce Elgort
# Date: July 22, 2017

def verse(number, action):
    # note how you can call functions within a print() function
    print(march(number), hurrah())
    print(march(number), hurrah())
    print(march(number))
    print(littleOne(action))
    # call the refrain() function
    refrain()


def march(number):
    # note how the statement below returns a string back to the calling statement
    return "The ants go marching %s by %s," % (number,number)


def hurrah():
    # note how the statement below returns a string back to the calling statement
    return "hurrah! hurrah!"


def littleOne(action):
    # note how the statement below returns a string back to the calling statement
    return "The little one stops to "+action+","


def refrain():
    print("And they all go marching down...")
    print("In the ground...")
    print("To get out...")
    print("Of the rain.")
    print("Boom! " * 3)


def main():
    # a list of tuples
    actions = [ ("one", "suck his thumb"),
                ("two", "tie his shoe"),
                ("three", "climb a tree"),
                ("four", "shut the door"),
                ("five", "take a dive"),
                ("six", "pick up sticks"),
                ("seven", "talk to Kevin"),
                ("eight", "jump the gate"),
                ("nine", "swing on a vine"),
                ("ten", "say 'The End'") ]

    # iterate through the actions list of tuples
    for n,a in actions:
        # call the verse() function with n and a as arguments
        verse(n,a)
        print()
    # press Enter key to Quit
    input("Press <Enter> to Quit")


main()