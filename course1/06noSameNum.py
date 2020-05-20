'''
pseudo code
def solution(arr):
    orderList = []
    orderList에 arr첫번재 원소 저장
    for in arr
        if arr's != pre
            change pre
            add orderList
    return orderList
'''



testlist = [7,7,2,3,9,5,5,5,5,0,0,0];


def solution(testlist):
    orderList = []
    pre = -1
    for i in testlist:
        if pre != i:
            pre = i
            orderList.append(pre)
    return orderList


print(solution(testlist))

'''
다른 사람 좋은 풀이

'''