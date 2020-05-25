'''
두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다.
 예를 들어 2와 7의 최소공배수는 14가 됩니다.
 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다.
 n개의 숫자를 담은 배열 arr이 입력되었을 때 이
  수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.


문제 분석... 나는 두개씩 최대공약수를 구해서  최종적으로 최대공약수를 구한다음에
전체 곱 / 최대공약수를 하기로 했다.

arr의 길이가 5라면
index 0 1
그다음 1 2
2 3
3 4
이렇게 4번만 하면 된다.
'''
'''
pseudo code

def solution(arr):
    for i in range(len(arr)-1):
        arr[i+1] = gcd(arr[i], arr[i+1])
    
    return mul(arr) / arr[-1]
    
'''

import math
def solution(arr):
    mulSum = arr[0]
    max = len(arr)-1
    for i in range(max):
        mulSum *= arr[i+1]
        arr[0] = math.gcd(arr[0], arr[i + 1])
    return  int(mulSum / math.pow(arr[0], max))
#
# def gcd(n, m):
#     res = n%m
#     if res == 0:
#         return m
#     return gcd(m, res)

#
# from math import gcd
#
# def solution(arr) :
#     def lcm(x,y) :
#         return x*y // gcd(x,y)
#     while True :
#         arr.append(lcm(arr.pop(),arr.pop()))
#         if len(arr) == 1 :
#             return arr[0]

'''

rom functools import reduce
from fractions import gcd

def nlcm(num):
    return reduce(lambda a, b : a * b // gcd(a, b), num)
'''