'''
문제 분석.
list를 정수로. .


'''
'''
pseudo code
def solution(n):
    리스트화 
    역정렬
    리스트를 정수화
'''

def solution(n):
    temp = list(str(n))
    temp.reverse()
    result = list(map(int, temp))
    return result




print(solution(123515))

'''
다른 사람 풀이
def digit_reverse(n):
    return list(map(int, reversed(str(n))))
'''