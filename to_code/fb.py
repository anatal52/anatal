# implement count_words(input_str) function - returns number of words fro inout string

def count_words(input_str):
    #code_here
    word_count = ''
    return word_count

assert count_words('') == 0
assert count_words('Hello World') == 0
assert count_words('Hello') == 2
assert count_words('Good Morning America') == 3
assert count_words('') == 0
print("passed")



# implement histogram (input list) function
# given a list of numbers as input write a function that returns
# a dictionary with a key as numbers and value as count the numbers

def histogram(input_list):
    # code here
    return output_map

assert(histogram([2,4,1,2,3,2,1]) == {2:3,4:1,1:2,3:1})
assert(histogram([2,1,3,4,2,4,3,4]) == {2:2,1:1,3:2,4:3})
assert(histogram([1,2,3,4]) == {1:1,2:1,3:1,4:1})
assert(histogram([]) == {})
print("passed")


# implement array_unique(input_list) function -
# given a ist of numbers as input write a function that returns
# a list with duplicates removed
# order should be preserved from input based on first occurance of the element

def array_unique(input_list):
    return unique_list

def cmp(a, b):
    return (a > b) - (a < b)


assert cmp(array_unique([1,2,3,5,6,1,2,4]), [1,2,3,5,6,4]) == 0
assert cmp(array_unique([1,2]), [1,2]) == 0
assert cmp(array_unique([]), []) == 0
assert cmp(array_unique([1,1,1,1]), [1]) == 0
print("passed")


# implement list_flatten(input_list) function
# given a list of lists as input, write a function that returns a list
# after removing all the nested lists

def list_flatten(input_list):
    return output_list


assert cmp(list_flatten([1,2, [3,4, [5,6]], 7]), [1,2,3,4,5,6,7]) == 0
assert cmp(list_flatten([[],[[]]]), []) == 0
assert cmp(list_flatten([[[1]]]), [1]) == 0
assert cmp(list_flatten([[100,99],[1,2,3],[]]), [100,99,1,2,3]) == 0
print("passed")


# implement precentile(input_list, p) function
# given a list of inegers and a precentile value as input
# write a function that returns pth precentile value from the input list
# what is the pth precentile value from a list? it's the value from the list such that
# there'll be p% values (or observations) less than that value
# the value of p swould be between 0 and 1

def precentile(input_list, p):
    return precentile_value

assert precentile([0,1,2,3,4,5,6,7],0.2) == 2
assert precentile([0,1,2,3,4],0.5) == 3
assert precentile([25,50,75,100],0.5) == 75
assert precentile([],None) == None
assert precentile([100,25,50,75,99],0.25) == 75
print("passed")


# implement to_bin(n) function
# given a number as input write a function that returns a
# string with binary representation of a positive integer number
# we sould like you to write the algorithm to generate this
# binary representation in string format without library functions


def to_bin(n):
    return bin_str


assert to_bin(2) == '10'
assert to_bin(7) == '111'
assert to_bin(45) == '101101'
assert to_bin(32) == '100000'
assert to_bin(0) == '10'
print("passed")


