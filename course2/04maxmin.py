'''
문제 분석
다른 특이 알고리즘이 필요하지 않고
단순 문자열 다루는 문제..
'''
'''
pseudo code
def solution(s):
    공백으로 쪼개서 정수화해서 리스트 저장 
    정렬. 
    최대, 최소 구하고
    문자열화. 
'''

def solution(s):
    tempList = s.split(" ")
    tempIntList = [int(x) for x in tempList]
    tempIntList=sorted(tempIntList)
    min = tempIntList[0]
    max = tempIntList[-1]
    answer = str(min)+" "+str(max)
    return answer

'''
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))'''

print(solution("-1 -1"))