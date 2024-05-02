"""
Given a string containing a number of characters, find the substrings within the string that satisfy
the conditions below:

- the substring's length should be in the inclusive interval [minLength, maxLength]
- the total number of unique characters should not exceed maxUnique

Using those conditions determine the frequency of maximum occuring substring
"""

from collections import Counter

def getmaxOccurances(comp, minLength, maxLength, maxUnique):
    n = len(comp)
    max_coocurances = 0

    for length in range(minLength, maxLength + 1):
        window = []
        char_count = Counter()
        unique_chars = 0

        for i in range(n):
            window.append(comp[i])
            char_count[comp[i]] += 1
            
            if len(window) > length:
                left_char = window.pop(0)
                char_count[left_char] -= 1
                if char_count[left_char] == 0:
                    del char_count[left_char]
            #print(char_count)
            if len(char_count) <= maxUnique:
                unique_chars = len(char_count)

            if len(window) == length and unique_chars <= maxUnique:
                substring = ''.join(window)
                #print(substring)
                #print(f'i :{i}', f'i - length + 1 :{i - length + 1}', sep='|')
                #count = comp.count(substring, i - length + 1, i + 1)
                count = comp.count(substring, i - length + 1)
                max_coocurances = max(max_coocurances, count)

    return max_coocurances


comp = 'abaabcdce'
minLength = 2
maxLegth = 3
maxUnique = 3

print(getmaxOccurances(comp, minLength, maxLegth, maxUnique))

comp = 'abdcadcabdcae'
minLength = 2
maxLegth = 4
maxUnique = 4

print(getmaxOccurances(comp, minLength, maxLegth, maxUnique))

