# EX 1 implement count_words(input_str) function - returns number of words from the input string
#
# def count_words(input_str):
#     print(input_str.split())
#     word_count = len(input_str.split())
#     return word_count
#
#
# assert count_words('') == 0
# assert count_words('Hello World') == 2
# assert count_words('Hello') == 1
# assert count_words('Good Morning America') == 3
# assert count_words(' connect the  world together ') == 4
# print("passed")


# EX 2 implement histogram (input list) function
# given a list of numbers as input write a function that returns
# a dictionary with a key as numbers and value as count the numbers

#
# def histogram(input_list):
#     # from collections import defaultdict
#     # output_map = defaultdict(int)
#     output_map = {}
#     for i in input_list:
#         if i not in output_map:
#             output_map[i] = 0
#         output_map[i] = output_map[i] + 1
#     return output_map
#
#
# assert (histogram([2, 4, 1, 2, 3, 2, 1]) == {2: 3, 4: 1, 1: 2, 3: 1})
# assert (histogram([2, 1, 3, 4, 2, 4, 3, 4]) == {2: 2, 1: 1, 3: 2, 4: 3})
# assert (histogram([1, 2, 3, 4]) == {1: 1, 2: 1, 3: 1, 4: 1})
# assert (histogram([]) == {})
# print("passed")


# EX 3 implement array_unique(input_list) function -
# given a ist of numbers as input write a function that returns
# a list with duplicates removed
# order should be preserved from input based on first occurrence of the element

# def array_unique(input_list):
#     unique_list = []
#     for i in input_list:
#         if i not in unique_list:
#             unique_list.append(i)
#     return unique_list
#

def cmp(a, b):
    return (a > b) - (a < b)


# assert cmp(array_unique([1,2,3,5,6,1,2,4]), [1,2,3,5,6,4]) == 0
# assert cmp(array_unique([1,2]), [1,2]) == 0
# assert cmp(array_unique([]), []) == 0
# assert cmp(array_unique([1,1,1,1]), [1]) == 0
# print("passed")
#
#
# EX 4 implement list_flatten(input_list) function
# given a list of lists as input, write a function that returns a list
# after removing all the nested lists

# def list_flatten(input_list):
#     output_list = []
#
#     def append_list(sublist):
#         for i in sublist:
#             if isinstance(i, int):
#                 output_list.append(i)
#             else:
#                 append_list(i)
#
#     append_list(input_list)
#     print(output_list)
#     return output_list
#
#
# assert cmp(list_flatten([1,2, [3,4, [5,6]], 7]), [1,2,3,4,5,6,7]) == 0
# assert cmp(list_flatten([[],[[]]]), []) == 0
# assert cmp(list_flatten([[[1]]]), [1]) == 0
# assert cmp(list_flatten([[100,99],[1,2,3],[]]), [100,99,1,2,3]) == 0
# print("passed")


# EX 5 implement percentile(input_list, p) function
# given a list of integers and a percentile value as input
# write a function that returns pth percentile value from the input list
# what is the pth percentile value from a list? it's the value from the list such that
# there'll be p% values (or observations) less than that value
# the value of p would be between 0 and 1

#
# def percentile(input_list, p):
#     from math import ceil
#     if input_list:
#         input_list.sort()
#         n = ceil(p * len(input_list))
#         percentile_value = input_list[n]
#         return percentile_value
#
# assert percentile([0,1,2,3,4,5,6,7],0.2) == 2
# assert percentile([0,1,2,3,4],0.5) == 3
# assert percentile([25,50,75,100],0.5) == 75
# assert percentile([],None) == None
# assert percentile([100,25,50,75,99],0.25) == 75
# print("passed")


# EX 6 implement to_bin(n) function
# given a number as input write a function that returns a
# string with binary representation of a positive integer number
# we would like you to write the algorithm to generate this
# binary representation in string format without library functions


def to_bin(n):
    bin_str = format(n, 'b')
    return bin_str


assert to_bin(2) == '10'
assert to_bin(7) == '111'
assert to_bin(45) == '101101'
assert to_bin(32) == '100000'
assert to_bin(0) == '0'
print("passed")


