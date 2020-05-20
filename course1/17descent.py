'''문제분석

역정렬
문자열화
'''

'''
pseudo code
def solution(s):
    temp = reverse sort
    result = join str
    return result
'''

def solution(s):
    temp = sorted(s, reverse=True)
    result = ''.join(temp)
    return result



'''
신기한 다른 사람 풀이

'''



print(solution("Zbcdefg"))