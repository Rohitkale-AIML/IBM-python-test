"""
Two strings are given, word and substr. Some of the characters in the word are a question mark '?'
Find te lexicographically smallest string that can be obtained by replacing '?' characters such that 
substr appears atleast once. If it is not possible to so so, return '-1'
"""

def getsmallestString(word, substr):
    n = len(word)
    m = len(substr)

    if m > n:
        return '-1'
    
    for start in range(n - m + 1):
        match = True
        result = list(word)
        #print(start)
        for i in range(m):
            #print(word[start + i])
            if word[start + i] == '?' or word[start + i] == substr[i]:
                result[start + i] = substr[i]
                #print(result[start + i])
            else:
                match = False
                break 
        if match:
            # check if there are any remaining '?' characters
            for j in range(n):
                if result[j] == '?':
                    result[j] = 'a' # lexicographically smallest character
            
            return ''.join(result)
    print(result)    
    return '-1'

word = 'as?b?e?gf'
substr = 'dbk'

print(getsmallestString(word, substr))