"""
For an array arr of n positive integers, count the unordered pairs (i, j) (0 <= i < j < n) 
where arr[i] XOR arr[j] > arr[i] AND arr[j]
"""

def dominating_xro_pairs(arr):
    n = len(arr)
    ans = 0

    for i in range(n):
        j = 0
        while j < n:
            if (i < j) and (arr[i] ^ arr[j]) > (arr[i] & arr[j]):
                #print(i,j)
                #print("XRO paris :", arr[i], arr[j])
                ans += 1
                
            j += 1
            
    return ans

if __name__ == '__main__':

    arr = [4, 3, 5, 2]
    print("dominating XRO pairs :", dominating_xro_pairs(arr))