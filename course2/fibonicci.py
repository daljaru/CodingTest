'''
2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

문제 분석.. 피보나치 수를 구현.
결과값을 123456로 나눈 나머지 리턴

다이나믹 프로그래밍 사용.
'''
'''
psedo code

fiboResult = []

def fino(n):
    n이 1이나 2면 fiboR [0 , 1]에 1저장. 
       
    if fiboR[n-1]이 null이 아니면. 
        fibo의 값을 fiboR에서 가져온걸로 더함.
    else:
        아니면 fiboR에 결과를 저장하고 더함.  
'''


def fibo(fValues, n):
    if n == 1 or n == 2:
        return fValues[n]
    else:
        if fValues[n] == 0:
            fValues[n] = fibo(fValues, n-1) + fValues[n-2]
            return fValues[n]
        else:
            return fValues[n-1] + fValues[n-2]
def solution(n):
    fValues = [0 for i in range(n+1)]
    fValues[0] = 0
    fValues[1] = 1
    fValues[2] = 1

    return fibo(fValues, n) % 1234567


print(solution(999))
