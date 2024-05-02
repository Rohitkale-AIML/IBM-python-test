"""
One of the shops in HackerMall is offering discount coupons based on a puzzling problem.
there are n tags where each tag has a value denoted by val[i]
a customer needs to choose the tags such a way that the sum of values is even.

the goal is to find maximum possible even sum of values of tags that can be chosen.
"""

def getMaximumEvenSum(arr):
    pos_num = 0

    # calculate sum of all positive elements
    for num in arr:
        if num > 0:
            pos_num += num 

    if pos_num % 2 == 0:
        return pos_num
    
    # check for each odd element 
    ans = -float('inf')
    for num in arr:
        if num % 2 != 0:
            #print(num)
            if num > 0:
                ans = max(ans, pos_num - num)
            else:
                ans = max(ans, pos_num + num)
            #print(ans)
    return ans

arr = [-1, -2, -3, 8, 7]

print(getMaximumEvenSum(arr))