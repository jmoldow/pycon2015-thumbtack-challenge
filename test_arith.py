#!/usr/bin/env python
# coding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals
import random
import subprocess
import sys

from arith import arith


def main():
    for _ in xrange(16):
        n = random.randint(3, 5)
        nums = [random.randint(0, 64) for _ in xrange(n + 1)]
        print(' '.join(map(str, nums)))
        arith(nums[-1], nums[:-1])
    return 0


if __name__ == '__main__':
    exit(main())
