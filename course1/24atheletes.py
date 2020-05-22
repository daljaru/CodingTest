'''문제분석
다른 리스트에 없는 값 빼오기

중복된 값도 있어서 머리를 써야한다.

'''


def solution(participant, completion):
    dict1 = {}
    dict2 = {}
    pSet = set(participant)
    for name in pSet:
        dict1[name] = participant.count(name)
        dict2[name] = completion.count(name)

    for comKey in dict2.keys():
        if dict1.get(comKey) != dict2.get(comKey):
            return comKey

    #result = [comKey for comKey in dict2.keys() if dict1.get(comKey) != dict2.get(comKey)][0]
    #return result



    #result = list(map(lambda compKeys : participant.pop(participant.index(compKeys)), dict2.keys()))

print(solution(	["leo", "kiki", "eden"], ["eden", "kiki"]))


'''
참고사이트
https://wayhome25.github.io/python/2017/06/14/time-complexity/
'''

'''시간초과
def solution(participant, completion):
    dict1 = {}
    dict2 = {}
    pSet = set(participant)
    for name in pSet:
        dict1[name] = participant.count(name)
        dict2[name] = completion.count(name)

    result = [comKey for comKey in dict2.keys() if dict1.get(comKey) != dict2.get(comKey)][0]
    return result
테스트 1 〉	통과 (0.05ms, 10.6MB)
테스트 2 〉	통과 (0.04ms, 10.7MB)
테스트 3 〉	통과 (5.91ms, 10.9MB)
테스트 4 〉	통과 (27.45ms, 11.1MB)
테스트 5 〉	통과 (21.35ms, 11.1MB)
'''

'''시간초과
def solution(participant, completion):
    dict1 = {}
    dict2 = {}
    pSet = set(participant)
    for name in pSet:
        dict1[name] = participant.count(name)
        dict2[name] = completion.count(name)

    result = [comKey for comKey in dict2.keys() if dict1.get(comKey) != dict2.get(comKey)][0]
    [dict1.pop(comKey) for comKey in dict2.keys() if dict1.get(comKey) == dict2.get(comKey)][0]
    return list(dict1.keys())[0]
테스트 1 〉	통과 (0.05ms, 10.6MB)
테스트 2 〉	통과 (0.04ms, 10.7MB)
테스트 3 〉	통과 (5.66ms, 10.8MB)
테스트 4 〉	통과 (22.71ms, 11.1MB)
테스트 5 〉	통과 (22.80ms, 11.1MB)
'''


'''시간초과
def solution(participant, completion):
    result = list(map(lambda comp : participant.pop(participant.index(comp)), completion))
    return participant[0]
    
테스트 1 〉	통과 (0.05ms, 10.7MB)
테스트 2 〉	통과 (0.05ms, 10.7MB)
테스트 3 〉	통과 (0.85ms, 10.8MB)
테스트 4 〉	통과 (3.05ms, 11MB)
테스트 5 〉	통과 (3.01ms, 11MB)    
'''


'''시간초과
def solution(participant, completion):
    setP = set(participant)
    return [person for person in setP if participant.count(person) != completion.count(person)][0]
테스트 1 〉	통과 (0.05ms, 10.8MB)
테스트 2 〉	통과 (0.04ms, 10.7MB)
테스트 3 〉	통과 (5.75ms, 10.9MB)
테스트 4 〉	통과 (21.05ms, 10.9MB)
테스트 5 〉	통과 (22.35ms, 11MB)
'''

'''시간초과
def solution(participant, completion):
    for person in set(participant):
        if(participant.count(person) != completion.count(person)):
            return person


테스트 1 〉	통과 (0.04ms, 10.6MB)
테스트 2 〉	통과 (0.04ms, 10.8MB)
테스트 3 〉	통과 (1.40ms, 10.8MB)
테스트 4 〉	통과 (3.84ms, 10.9MB)
테스트 5 〉	통과 (17.89ms, 11MB)
'''


'''이것도 시간초과
def solution(participant, completion):
    for person in participant:
        if(participant.count(person) != completion.count(person)):
            return person
테스트 1 〉	통과 (0.04ms, 10.7MB)
테스트 2 〉	통과 (0.04ms, 10.7MB)
테스트 3 〉	통과 (0.96ms, 10.9MB)
테스트 4 〉	통과 (10.95ms, 11MB)
테스트 5 〉	통과 (1.11ms, 11MB)
'''

'''
def solution(participant, completion):
    for comp in completion:
        idx = participant.index(comp)
        participant.pop(idx)

    return participant[0]
    
이것도 시간 초과.
테스트 1 〉	통과 (0.04ms, 10.7MB)
테스트 2 〉	통과 (0.04ms, 10.8MB)
테스트 3 〉	통과 (0.80ms, 10.9MB)
테스트 4 〉	통과 (2.99ms, 11MB)
테스트 5 〉	통과 (2.95ms, 11MB)
'''

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
테스트 1 〉	통과 (0.05ms, 10.8MB)
테스트 2 〉	통과 (0.05ms, 10.7MB)
테스트 3 〉	통과 (5.48ms, 10.9MB)
테스트 4 〉	통과 (22.62ms, 11MB)
테스트 5 〉	통과 (22.62ms, 11.1MB)
'''

'''문제분석 실패
def solution(participant, completion):
    partList = sorted(set(participant))
    compList = sorted(set(completion))
    minLen = len(compList)
    result = partList[minLen:]
    return result[0] if len(result) > 0 else ""
'''



'''
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
    
    
    
def solution(participant, completion):  # 환상적인 코드. 
    answer = ''
    temp = 0
    dic = {}
    for part in participant:     #참가자 이름의 해시값. ... . . 해시값을 키로. 이름을 값으로.  크.... 지렸다. 
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
    
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]    
'''

