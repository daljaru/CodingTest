'''
문제분석
최대공약수 최소공배수

'''

'''
pseudocode
def gcd(n, m)
    유클리디안 기반 재귀함수. 

최소공배수 = 두수 곱셈 / 최대공약수
'''
def gcd(n, m):
    res = n%m
    if res == 0:
        return m
    return gcd(m, res)


def solution(n, m):
    gcdResult = gcd(n, m)
    result = [gcdResult, n*m//gcdResult]
    return result

print(solution(10,6))