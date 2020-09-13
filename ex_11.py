# https://www.tocode.co.il/bundles/python/lessons/11-syntax-lab


# 1. user input 10 nums, print max
def ex_11_1():
    nums = []
    for i in range(10):
        num = int(input("Please enter a number: "))
        nums.append(num)
    print("The biggest number is: %d" % max(nums))
