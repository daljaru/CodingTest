'''
문제분석
예전 문제 활용

'''

'''
pseudo code
def solution(x):
    각자리숫자 합 구하기
    나눠서 떨어지는지 확인
    return 결과
'''


def addNumPos(n):
    total = 0
    for i in list(str(n)):
        total += int(i)
    return total


def solution(x):

    sumNumPos = addNumPos(x)
    return True if x%sumNumPos == 0 else False