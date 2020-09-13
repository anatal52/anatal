# https://www.tocode.co.il/bundles/python/lessons/05-intro-lab

# 1. user input age in years, print output age in months
age1 = input("How old are you in years? ")
age1_months = float(age1)*12
print("You age in months is %d" % age1_months)

"""
Uri's comments:
==============

* Very good! This code works.
* It's better to use .gitignore to not commit .idea files to the repository
  (PyCharm internal files).
* It's better to avoid using digits in variable names usually. You can separate 
  each exercise to a separate file.
* I recommend styling your code according to PEP-8. You can also use PyCharm's
  Code -> Reformat Code feature. For example, spaces around "*", spaces after comma etc.
  This is relevant to all your exercises.
* Here is how your code looks reformatted:

# 1. user input age in years, print output age in months
age = input("How old are you in years? ")
age_months = float(age) * 12
print("You age in months is %d" % age_months)

"""

# 2. user input age in years, print output age in months
age2_months = input("How old are you in months? ")
age2 = float(age2_months)/12
print("You're %.2f years old" % age2)

"""
Uri's comments:
==============

* Very good! This code works.

"""

# 3. 7 Boom if num / 7
num = input("Choose any number and enter: ")
if int(num) % 7 == 0:
    print("Boom!")

"""
Uri's comments:
==============

* Very good! This code works.

"""

# 4. 7 Boom if num / 7 or contains 7
num = input("Choose any number and enter: ")
if int(num) % 7 == 0 or '7' in num:
    print("Boom!")

"""
Uri's comments:
==============

* Very good! This code works.
* `if int(num) % 7 == 0 or '7' in num` is correct, however I recommend adding
  parentheses so it would be more readable.
* Here is how your code looks reformatted:

# 4. 7 Boom if num / 7 or contains 7
num = input("Choose any number and enter: ")
if (int(num) % 7 == 0) or ('7' in num):
    print("Boom!")

"""

# 5. input 3 numbers print max
nums = []
for i in range(3):
    num = input("Enter a number: ")
    nums.append(int(num))
print("Biggest number is %d " % max(nums))

"""
Uri's comments:
==============

* Very good! This code works.
* It's very good you used the built-in function "max".
  Built-in Functions in Python: https://docs.python.org/3/library/functions.html

"""

# 6. arithmetic progression #https://en.wikipedia.org/wiki/Arithmetic_progression
a1 = int(input("We're going to generatae an arithmetic sequence,\nEnter the first number in sequence: "))
d = int(input("Enter the difference: "))
n = int(input("Enter number of elements: "))
sn = n/2 * (2*a1 + (n-1) * d)
print('Sum is % d' % sn)

"""
Uri's comments:
==============

* Very good! This code works.
* Typo in "generatae".

"""
