'''
pseudo code

def solution(seoul):
    name = "Kim"
    index = 0
    for seoul
        if Kim
            break
        index += 1
    
    answer = "~~"
    return answer

'''

def solution(seoul):
    name = "Kim"
    index = 0
    for i in seoul:
        if i == name:
            break
        index += 1

    answer = '김서방은 {}에 있다'.format(index)
    return answer

'''
다른 좋은 풀이
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))
'''