'''
문제분석.
타입변환 문제같다.

for i in 리스트변환한 숫자.
    각 숫자를 정수형변환.
    더하기
    리턴 총합

'''


def solution(n):
    total = 0
    for i in list(str(n)):
        total += int(i)
    return total


print(solution(123))


'''
신기한 다른 사람코드
def sum_digit(number):
    return sum(map(int,str(number)))
'''