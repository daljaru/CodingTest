

'''
pseudocode

set으로 만들어서

절반의 길이보다 크면 set길이,
작으면 절반의 길이 반환.

'''

def solution(nums):

    pickNum = int(len(nums) / 2)

    testSet = set(nums)
    setLength = len(testSet)

    if(setLength > pickNum):
        return pickNum
    else:
        return setLength


'''
신기한 다른사람 풀이
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
'''

testList = [3,3,3,2,2,4]

print(solution(testList))