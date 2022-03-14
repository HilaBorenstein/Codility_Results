# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    binary=bin(N)[2:]
    binary_str=str(bin(N)[2:])
    max_count=0
    cur_count=0
    #print(binary_str)
    for i in binary_str:
        if int(i)==0:
            cur_count=cur_count+1
        elif int(i)==1:
            if cur_count>max_count:
                max_count=cur_count
            cur_count=0

    
    return max_count