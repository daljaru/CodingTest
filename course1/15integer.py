'''
문제분석 : math모듈 import
sqrt()활용
'''

'''
pseudo code

def solution(n):
    sqrt(n)
    
    딱 정수와 맞으면
        pow(num+1, 2)
    아니면 -1 리턴
'''
import math

def solution(n):
    sq = math.sqrt(n)
    if sq == int(sq):
        return math.pow(sq+1,2)
    else:
        return -1



# print(solution(9))

'''
신기한 다른사람 코드
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'
'''
