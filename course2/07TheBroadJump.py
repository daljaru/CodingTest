'''
효진이는 멀리 뛰기를 연습하고 있습니다. 효진이는 한번에 1칸, 또는 2칸을 뛸 수 있습니다. 칸이 총 4개 있을 때, 효진이는
(1칸, 1칸, 1칸, 1칸)
(1칸, 2칸, 1칸)
(1칸, 1칸, 2칸)
(2칸, 1칸, 1칸)
(2칸, 2칸)
의 5가지 방법으로 맨 끝 칸에 도달할 수 있습니다. 멀리뛰기에 사용될 칸의 수 n이 주어질 때, 효진이가 끝에 도달하는 방법이 몇 가지인지 알아내,
 여기에 1234567를 나눈 나머지를 리턴하는 함수, solution을 완성하세요.
 예를 들어 4가 입력된다면, 5를 return하면 됩니다.

제한 사항
n은 1 이상, 2000 이하인 정수입니다.
입출력 예
n	result
4	5
3	3
입출력 예 설명
입출력 예 #1
위에서 설명한 내용과 같습니다.

입출력 예 #2
(2칸, 1칸)
(1칸, 2칸)
(1칸, 1칸, 1칸)
총 3가지 방법으로 멀리 뛸 수 있습니다.



몇개 적어보니 피보나치 수열이였다.


'''


'''
피보나치를 계산해서 
1234567로 나누자. 

'''


def fibo(n, fValues):
    if n == 1 or n == 2:
        return fValues[n-1]
    else:
        for i in range(2, n):#0 1 2
            fValues[i] = fValues[i-1]+fValues[i-2]

    return fValues[-1] # 만약 n이 4이면 index 1, 2를 가져와야 하므로

def solution(n):
    n = n+1
    fValues = [0 for i in range(n)]
    fValues[0] = 1
    fValues[1] = 1
    fiboNumber = fibo(n, fValues)
    return fiboNumber%1234567

print(solution(5))