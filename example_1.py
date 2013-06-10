# We want the following function to return a sorted array of n random numbers
# between 0 and 1. But it doesn't currently:
#
# $ python example_1.py
# Sorted random values:  None
#
# Why does it not work?
# It does not work because x.sort() is only defined for list and returns None.
# The following is so that it works with Python 3 too
from __future__ import print_function

import numpy as np


def sorted_random_array(n):
    x = np.random.random(n)
    return sorted(x)

print("Sorted random values: ", sorted_random_array(10))
