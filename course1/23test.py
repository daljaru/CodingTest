'''
문제 분석.

세사람의 찍기 배열이 주어지고
arr1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5...] 12345
arr2 = [ 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2,...]   21232425
arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4...] 3311224455



'''

def solution(answers): #answer는 정답리스트
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]

    answersLen = len(answers)
    p1Len = len(p1)




    result = list(map(lambda x : x==x, p1))  # p1의 각 원소를 비교한 결과를 리스트에 넣어야함.

    return answers  #가장 많은 문제를 맞힌 사람이 누구인지 배열에 담기



print(solution([1,3,2,4,2,3,4,2,1,3,2,4,5,3,2,4,3,3,4,2,4,2]))

