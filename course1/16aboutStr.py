'''
문제분석 : 문자열 길이, isnumeric

'''
'''
pseudo code
def solution(s):
    len()
    if len 4 or 6
        if isnum
            return True
        else ret False
    ret False
'''

def solution(s):
    length = len(s)
    if length == 4 or length == 6:
        if s.isnumeric():
            return True
        else:
            return False
    else:
        return False





print(solution("1234567"))


'''
신기한 다른 사람 코드
def alpha_string46(s):   정규화 사용
    import re
    return bool(re.match("^(\d{4}|\d{6})$", s))

def alpha_string46(s):   in도 활용...
    return s.isdigit() and len(s) in (4, 6)

'''