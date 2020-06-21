import math

def solution(n,a,b):
    preA = a
    preB = b
    count = 1
    while(preA != preB):
        preA = math.ceil(preA / 2)
        preB = math.ceil(preB / 2)
        count += 1
    return count-1

print(solution(8, 4, 7))