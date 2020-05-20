'''
pseudo code
짝수면
    가운데 두개 슬라이스
홀수면
    가운데
'''



def solution(s):
    strLen = len(s)
    pos = strLen//2
    if len(s)%2 == 0:
        return s[pos-1:pos+1]
    else:
        return s[pos]


'''
다른 사람 좋은 풀이
def string_middle(str):
    return str[(len(str)-1)//2:len(str)//2+1]
'''