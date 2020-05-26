'''

문제 분석
나는 yellow의 약수의 쌍을 구하고
그 약수의 쌍에서 brown 총 개수를 구한뒤 인자 brown과 같으면
전체 사이즈를 리턴하는 방법을 사용했다.
약수를 저장하는 방법은 dictionary를 사용하는데 이게 효율적인지는 잘 모르겠다.
'''


def solution(brown, yellow):
    dict = {}
    width = 0
    height = 0
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            if dict.get(i) != None:
                break
            n = yellow//i
            dict[n] = i
            if (4 + 2 * (n+i)) == brown:
                width = n+2
                height = i+2
    answer = []
    answer.append(width)
    answer.append(height)
    return answer



print(solution(24, 24))