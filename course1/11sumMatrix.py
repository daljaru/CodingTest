'''
문제 분석.

반복을 반드시 두번써야하긴 함.

pseudo code

list comprehension [두번 반복.  원소끼리 더할 때는zip이용.]

'''


def solution(arr1, arr2):
    result = [[sum(j) for j in zip(arr1[i], arr2[i])] for i in range(len(arr1))]
    return result

print(solution([[1,2],[2,3]],[[3,4],[5,6]]))

'''
좋았던 다른 사람 풀이
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer
'''