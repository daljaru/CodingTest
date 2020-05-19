'''
psuedo code:
 if 짝수 : 수박 * 짝수 /2
 if 홀수 : 홀수 /2 + 수
'''


def solution(n):
    if n%2 == 0:
        answer = '수박'*(n//2)
    else:
        answer = '수박'*(n//2) + '수'
    return answer



print(solution(5))

'''
좋았던 다른 사람 코드
def water_melon(n):
    s = "수박" * n
    return s[:n]
    
def water_melon(n):
    return "수박"*(n//2) + "수"*(n%2)   홀수면이니까.. %를 씀..
    
    
'''