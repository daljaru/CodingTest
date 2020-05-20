def solution(participant, completion):
    dict1 = {}
    for name in set(participant):
        dict1[name] = participant.count(name)

    print(dict1)




print(solution(["marina", "marina", "filipa", "filipa", "josipa"], ["marina", "marina", "filipa", "filipa"]))


'''
효율설 zero코드.
def solution(participant, completion):
    dict1 = {}
    dict2 = {}
    resultDict = {}
    set(participant)
    for name in set(participant):
        dict1[name] = participant.count(name)
        dict2[name] = completion.count(name)

    for name in dict1.keys():
        partNum = dict1.get(name)
        compleNum = dict2.get(name)
        if partNum > compleNum:
            resultDict[name] = partNum - compleNum

    result = list(resultDict)
    return result[0]
'''

'''문제분석 실패
def solution(participant, completion):
    partList = sorted(set(participant))
    compList = sorted(set(completion))
    minLen = len(compList)
    result = partList[minLen:]
    return result[0] if len(result) > 0 else ""
'''





