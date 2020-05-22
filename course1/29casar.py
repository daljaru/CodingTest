'''문제분석
dictionary를 쓰자.

'''

def solution(s, n):
    allalpha = "abcdefghijklmnopqrstuvwxyz"
    allalphaList = list(allalpha)
    num_alpha = {i : allalphaList[i] for i in range(len(allalpha))}
    alpha_num = {allalphaList[i] : i for i in range(len(allalpha))}

    result = ""

    for i in s:
        flag = True
        if i.isupper():
            flag = False
            i = i.lower()
        if(i in alpha_num.keys()):
            num = alpha_num.get(i)
            num += n
            num %= 26
            alpha = num_alpha.get(num)
            if flag == False:
                alpha = alpha.upper()
            result += alpha
        else:
            result += " "
    return result


print(solution("z", 1))


'''
다른 사람 신기한 코드
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
    # 주어진 문장을 암호화하여 반환하세요.


# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))
'''