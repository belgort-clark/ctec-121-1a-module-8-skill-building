# Module 6 - Skill Building Exercise No. 6 Solution
# Author: Bruce Elgort
# Date: July 22, 2017

def grade(score):
    return "FFDCBA"[score]


def main():
    print("Quiz Grader")
    score = eval(input("Enter the score (0-5): "))
    print("The grade is", grade(score))


main()
