import math
import collections


def solution(progresses, speeds):
    answer = []

    q = collections.deque()

    for progress, speed in zip(progresses, speeds):
        residum =  100-progress
        workDay = math.ceil(residum / speed)
        q.append(workDay)

    first = q.popleft()
    count = 1

    while(True):
        workDay = q.popleft()
        if first >= workDay:
            count += 1
        elif first < workDay:
            answer.append(count)
            first = workDay
            count = 1

        if(len(q) == 0):
            answer.append(count)
            break

    return answer



progresses = [93,30,55]
speeds = [1,30,5]

print(solution(progresses, speeds))
