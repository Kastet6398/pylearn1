import os
import sys
import timeit# a generator that yields items instead of returning a list
sys.set_int_max_str_digits(sys.maxsize // 10000000000)
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(range(sys.maxsize ** 999))
print(timeit.timeit("sum(firstn(1000000))", globals={"firstn": firstn}, number=1))
print(timeit.timeit("sum(range(1000000))", globals={"firstn": firstn}, number=1))