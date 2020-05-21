'''
문제 분석.

세사람의 찍기 배열이 주어지고
arr1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5...] 12345
arr2 = [ 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2,...]   21232425
arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4...] 3311224455

정답은 랜덤으로 주어지는데.....
'''

from itertools import cycle

def checkAnswer(pAnswer, answers):
    count = 0
    for i in range(len(pAnswer)):
        if pAnswer[i] == answers[i]:
            count += 1
    return count

def solution(answers): #answer는 정답리스트
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]

    persons = [p1, p2, p3]
    result = []
    for person in persons:
        pCycle = cycle(person)
        pAnswer = [next(pCycle) for i in range(len(answers))]
        result.append(checkAnswer(pAnswer, answers))

    result = [i+1 for i in range(len(result)) if result[i] == max(result)]
    return result


print(solution([1,3,4,4,2,3,4,2,1,3,2,4,1,3,2,4,3,3,4,2,4,2]))


'''다른 사람 신기한 풀이
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
'''