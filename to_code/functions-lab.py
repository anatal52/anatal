# https://www.tocode.co.il/bundles/advanced-pytho4n3/lessons/functions-lab

# 1 Parameters
def mul_args(*args):
    i = 1
    for arg in args:
        if type(arg) in [float, int]:
            i *= arg
    return i


def groupby(*args):
    from collections import defaultdict
    d = defaultdict(list)
    f = args[0]
    for arg in args[1:]:
        d[f(arg)].append(arg)
    print(dict(d))

# returns: { h: ['hello', 'hi', 'help', 'here'], b: ['bye'] }
# groupby(lambda s: s[0], 'hello', 'hi', 'help', 'bye', 'here')


# 2 Decorators

def after5(f):
    calls = 0
    def helper():
        nonlocal calls
        calls += 1
        if calls > 5:
            return f()
    return helper


@after5
def doit():
    print("Yo!")

# doit()
# doit()
# doit()
# doit()
# doit()
# doit()

######################

def memoize(f):
    vals = {}
    def wrapper(n):
        nonlocal vals
        if n not in vals:
            vals[n] = f(n)
            return f(n)
        else:
            return vals[n]
    return wrapper


@memoize
def fib(n):
    print(f"fib({n})")
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# print(fib(10))

######################

def returns(type):
    def decorator(f):
        def wrapper(arg):
            if isinstance(arg, type):
                return f(arg)
            else:
                raise AssertionError(f"{arg} is not type {type}")
        return wrapper
    return decorator

@returns(str)
def same(word):
    return word

# works:
# print(same('hello'))

# raise AssertionError:
# same(10)

# Generators

# 1 natural number squares

# def fib():
#     x, y = 1, 1
#     while True:
#         yield x
#         x, y = y, x+ y
#
# g = fib()
# print(next(g))

import itertools as it

def next():
    x = 1
    while True:
        yield x
        x += 1

sq_next = (x * x for x in next())

for val in it.islice(sq_next, 10):
    print(val)


# 2 uniq sequence

def uniq(list):
    return set(list)

print(uniq([2,2,2,3,4,5,1,1,1]))

# find
