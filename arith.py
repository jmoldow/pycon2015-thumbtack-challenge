#!/usr/bin/env python
# coding: utf-8

from __future__ import division, print_function, unicode_literals
from itertools import combinations_with_replacement, chain, ifilter, imap, izip, izip_longest, permutations, product
from operator import add, sub, mul, truediv
import sys


operations = [add, sub, mul, truediv]

def op_repr(op):
    return {
        add: '+',
        sub: '-',
        mul: '*',
        truediv: '/',
    }[op]

def operator_combinations(num_ops):
    return combinations_with_replacement(operations, num_ops)

def arith_combinations(numbers):
    num_ops = len(numbers) - 1
    return product(permutations(numbers), operator_combinations(num_ops))

def arith_sum(arith):
    numbers, ops = arith
    ops = chain([add], ops)
    result = 0
    for (num, op) in izip(numbers, ops):
        result = op(result, num)
    return result

def check(desired_sum, arith):
    try:
        return arith_sum(arith) == desired_sum
    except ZeroDivisionError:
        return False

def arith(desired_sum, numbers):
    valid_ariths = ifilter(lambda arith: check(desired_sum, arith), arith_combinations(numbers))
    arith = next(valid_ariths, None)
    if arith:
        nums, ops = arith
        for (num, op) in izip_longest(nums, ops, fillvalue=None):
            print('{}{}'.format(num, ' {} '.format(op_repr(op)) if op else ''), end='')
        print()


def _readlines():
    while True:
        line = sys.stdin.readline().strip()
        if line:
            yield line
        else:
            return


def main():
    for line in _readlines():
        if '-d' in sys.argv:
            print(line)
        numbers = map(int, line.split(' '))
        arith(numbers[-1], numbers[:-1])
    return 0


if __name__ == '__main__':
    exit(main())
