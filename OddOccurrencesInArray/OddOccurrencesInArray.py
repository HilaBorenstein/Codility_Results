# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import Counter

def solution(A):
    # write your code in Python 3.6
    my_dict=Counter(A)
    for key, value in my_dict.items():
        if value%2!=0:
            res=key
        #print(key, '->', value)
    return res

''' Other Option
def solution(A):
    # write your code in Python 3.6

    counts = dict()
    for i in A:
        counts[i] = counts.get(i, 0) + 1

    for key, value in counts.items():
        if value%2!=0:
            res=key
        #print(key, '->', value)
    return res
    '''