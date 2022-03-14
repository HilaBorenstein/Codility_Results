# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    l=len(A)
    rotate_arr=[None] * l
    for i in range(len(A)):
        new_place=(i+K)% l
        rotate_arr[new_place]=A[i]
    return rotate_arr

''' Other option:
def solution(A, K):
    l=len(A)
    rotate_arr=[None] * l
    for  i, value in enumerate(A):
        new_place=(i+K)% l
        rotate_arr[new_place]=value
    return rotate_arr

'''