'''
문제분석
리스트 슬라이싱, 정렬
'''
'''
pseudo code
def solution(arr, comms):
    result = []
    for in comms:
        slice
        sort
        result.append(arr[index])
    return result
'''

def solution(array, commands):
    result = []
    for command in commands:
        testSlice = array[command[0]-1:command[1]]
        testSorted = sorted(testSlice)
        result.append(testSorted[command[2]-1])

    return result


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))


'''
다른사람 코드

def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
    
    
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
'''