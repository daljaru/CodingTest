'''

문제 분석.

나는 배열 A에서 제일 작은 값이
배열 B의 제일 큰값부터 차례대로 곱하면 된다고 생각했다.
'''
'''
pseudo code
def solution(A, B):
    A 정렬
    B 정렬 > 거꾸로 정렬
    
    각 값 처음부터 차례대로 서로 곱해서 더한값 total에 넣기 
    total 리턴
'''

def solution(A,B):
    A.sort()
    B.sort()
    B.reverse()
    total = 0
    for i in range(len(A)):
        total += A[i]*B[i]

    return total




print(solution([1, 4, 2],	[3, 6, 4]))