"""
package docstring here
"""
# star means import all names
# .queue represents the subdirectory queue, and within that subdirectory
# there is another __init__.py that imports all the names from queue.py
# main benefit is you can directly access StatelessQueue without doing
# cmsc142.queue.StatelessQueue

from .misc import *
from .queue import *
from .stack import *
from .trees import *


def merge_sort(array):
    if len(array) <= 1:
        return array
    
    midIdx = len(array) // 2
    leftSorted = merge_sort(array[:midIdx])
    rightSorted = merge_sort(array[midIdx:])

    return merge(leftSorted, rightSorted)

def merge(left, right):
    merged = []
    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    
    merged += left
    merged += right

    return merged

def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst) - 1))