# https://www.tocode.co.il/bundles/python/lessons/11-syntax-lab
from random import randint


# 1. user input 10 nums, print max
def ex11_1():
    nums = []
    for i in range(1, 11):
        num = int(input("Please enter a number #%d: " % i))
        nums.append(num)
    print("The biggest number is: %d" % max(nums))


"""
Uri's comments:
==============

* This function works, but you didn't run it. You should run it from the main file.
* It's better to write each assignment in a different file.
* If you don't need i to start with 1, you can just use and it's more common to use range(10).

"""

# 2. Input age print months with error
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
            return
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
