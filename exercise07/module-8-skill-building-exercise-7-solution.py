# Module 8 - Skill Building Exercise No. 7 Solution
# Author: Bruce Elgort
# Date: July 22, 2017

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2


def test():
    nums = list(range(10))
    squareEach(nums)
    print(nums)


test()
