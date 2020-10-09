# https://www.tocode.co.il/bundles/python/lessons/11-syntax-lab
from random import randint


# 1. user input 10 nums, print max
def ex11_1():
    nums = []
    for i in range(1, 11):
        # 1. Using %d is a bit outdated. Today it is considered more modern to use f{} strings:
        # Please see lesson here:
        # https://www.tocode.co.il/bundles/advanced-python3/lessons/python3-cool-features
        num = int(input(f"Please enter a number #{i}: "))
        nums.append(num)
    print(f"The biggest number is: {max(nums)}")

    # 2. Look at the pattern here: You create a list (nums = []), then you iterate over some other stuff and each iteration
    #    creates a new item in the list. This is exactly a list comprehension.
    #    A better way to write the previous loop is therefore:
    nums = [int(input(f("Please enter a number #{i + 1}: "))) for i in range(10)]

    # 3.But actually we don't need the "remember" all the values and search for the
    #   maximum in the end. It would be more memory efficient to just keep track of the maximum values
    #   as numbers arrive:
    max_num = float('-inf')
    for i in range(10):
        num = int(input(f"Please enter a number #{i}: "))
        max_num = max(num, max_num)
    print(max_num)

    # 4. Some weird people would combine 2 and 3 to get this:
    from functools import reduce
    reduce(max, (int(input(f"Please enter a number #{i + 1}: ")) for i in range(10)), float('-inf'))
    # This is very interesting because, like (3), it won't keep all the values in memory,
    # but at the same time uses the short comprehension syntax.
    # For more information about how it works please watch this lesson:
    # https://www.tocode.co.il/bundles/advanced-python3/lessons/generators

"""
Uri's comments:
==============

* This function works, but you didn't run it. You should run it from the main file.
* It's better to write each assignment in a different file.
* If you don't need i to start with 1, you can just use and it's more common to use range(10).

"""

# 2. Input age print months with error
# In the example here:
# https://www.tocode.co.il/bundles/python/lessons/10-exceptions
# I demonstrate how to write a function "read_number_stubbornly" (you can read about it in the text tab if you don't have time to watch the video)
# Such a function will help to simplify your code below
def ex11_2():
    i = 0
    while True:
        try:
            if i == 0:
                prompt = "Enter your age: "
            else:
                prompt = "This can't be your age, please try again: "
            age = int(input(prompt))
            print("Your age in months is %d" % age)
            return
        except ValueError:
            i += 1

"""
Uri's comments:
==============

* You print the input, this is not what the assignment expects. The input is in years and 
  the assignment expect you to convert it to months. Please try again.

"""

# read and print until empty row
def ex11_3():
    big_string = ""
    line = "\n"
    while line:
        line = input("Enter a line: ")
        big_string += line+"\n"
    print(big_string.rstrip("\n"))

"""
Uri's comments:
==============

* You forgot to reverse the lines before printing.

"""

# find int % 7, 13, 15
def ex11_4():
    while True:
        x = random.randint(1, 1000000)
        if (x % 7 == 0) and (x % 13 == 0) and (x % 15 == 0):
            print("The number %d meets the criteria! Yay :)" % x)
            # I think "break" is more fitting here
            break
        else:
            print("The number %d doesn't meets the criteria, we'll try again" % x)
    print(x)

"""
Uri's comments:
==============

* You used "random" but didn't import it. If you want to use "randint" after 
  you imported it, just use "randint".
  PyCharm also warns about it.

"""

# find least common multiple
def ex11_5():
    x = randint(1, 10)
    y = randint(1, 10)
    z = min(x, y)
    while True:
        if z % x == 0 and z % y == 0:
            print("Least common multiple of %d,%d is %d" % (x, y, z))
            return
        else:
            z += 1

"""
Uri's comments:
==============

* Very good! This code works.
* Just a note - this works for numbers <= 10, but if the numbers would be
  bigger (~6 digits or more), then this algorithm is very unefficient,
  and there are algorithms which are much more efficient.
  
"""

# guess a number 1-100
def ex11_6():
    x = randint(1, 100)
    print("[The secret number is %d sssshhhhh...]" % x)
    while True:
        y = int(input("Guess a number from 1 to 100: "))
        if y == x:
            print("Bingo %d!" % y)
            return
        if y < x or randint(x, x+10) == x:
            print("you guessed too low")
        elif y > x or randint(x-10, x) == x:
            print("you guessed too high")


if __name__ == '__main__':
    ex11_6()

"""
Uri's comments:
==============

* Very good! This code works.
* If you want the user to guess the number, don't print it.
  
"""
