'''문제분석

list comprehension
삼항연산자 쓰기

'''
'''
pseudo code
def solution(arr, div):
    나눠지면 list comprehention
    길이가 0이면 -1 아니면 정렬된거 리턴. 
'''

def solution(arr, divisor):
    tempList = [num for num in arr if num % divisor == 0]
    return [-1] if len(tempList) == 0 else sorted(tempList)



print(solution([5, 9, 7, 10],1))