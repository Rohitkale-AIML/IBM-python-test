"""
Given an array arr of n integers, a sequence of n-1 operations must be performed on the array.

In each operation,
- Remove the minimum and maximum elements from the current array and add their sum back to array
- The cost of an operation cost= ceil((min_ele + max-ele)/(max_ele - min-ele + 1))

Find the total cost to reduce the array to a single element
"""

import math

def findTotalCost(arr):
    total_cost = 0

    while len(arr) > 1:
        min_element = min(arr)
        max_element = max(arr)

        cost = math.ceil((min_element + max_element) / (max_element - min_element + 1))

        arr.remove(min_element)
        arr.remove(max_element)

        arr.append(min_element + max_element)

        total_cost += cost
    
    return total_cost

arr = [2, 3, 4, 5, 7]
print(findTotalCost(arr))

arr = [8, 8, 8, 8]
print(findTotalCost(arr))