
'''

문제분석
replace 쓰기

'''
'''
pseudo code:
def solution(str):
    뒤에서 5번째 전까지 자름.
    그걸 *로 다 바꿈.
    리턴 결과. 
'''
def solution(phone_number):
    replaceStr = phone_number[0:-4]
    phone_number = phone_number.replace(replaceStr, "*"*len(replaceStr))
    return phone_number

print(solution("01033334wefqwef444"))