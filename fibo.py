'''Dammy Olude 100888626'''


def fib1(n):
    a, b = 0, 1    #define a and b as 0 and 1
    for _ in range(n):  # executing a loop for n times
        print(a, end='')   # prints the variable a
        a, b = b, a + b   # it makes the variable a equals to value of the variable b and makes b equal to the result of a + b
pass


def fib2(n):
    result = []  # We will store our result in this list
    a, b = 0, 1
    for _ in range(n):
        result.append(a)  # adds variable a to the list
        a, b = b, a + b

    return result

