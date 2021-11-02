# Module 8 - Skill Building Exercise No. 8 Solution
# Author: Bruce Elgort
# Date: July 22, 2017

def main():
    print("Number of years for an investment to double.\n")

    apr = eval(input("What is the annual interest rate? "))
    principal = 1
    years = 0
    while principal < 2:
        principal = principal * (1 + apr)
        years = years + 1

    print("Years to double:", years)


# Do you know what this does? There's a video on it in Canvas Week 2
# If you read this go to Slack and Direct Message me for extra credit
if __name__ == '__main__':
    main()
