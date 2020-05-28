'''

한 번에 K 칸 점프 or (현재까지 온 거리) x 2 에 해당하는 위치로 순간이동
index + k          [index*2]
k개 건전지 소모       소모 0

거리가 N 만큼 떨어져 있는 장소로 가려고 합니다.
점프로 이동하는 것은 최소로 하려고 합니다.


예를 들어 거리가 5만큼 떨어져 있는 장소로 가려고 합니다.
아이언 슈트를 입고 거리가 5만큼 떨어져 있는 장소로 갈 수 있는 경우의 수는 여러 가지입니다.

처음 위치 0 에서 5 칸을 앞으로 점프하면 바로 도착하지만, 건전지 사용량이 5 만큼 듭니다.
처음 위치 0 에서 2 칸을 앞으로 점프한 다음 순간이동 하면 (현재까지 온 거리 : 2) x 2에 해당하는 위치로 이동할 수 있으므로 위치 4로 이동합니다. 이때 1 칸을 앞으로 점프하면 도착하므로 건전지 사용량이 3 만큼 듭니다.
처음 위치 0 에서 1 칸을 앞으로 점프한 다음 순간이동 하면 (현재까지 온 거리 : 1) x 2에 해당하는 위치로 이동할 수 있으므로 위치 2로 이동됩니다. 이때 다시 순간이동 하면 (현재까지 온 거리 : 2) x 2 만큼 이동할 수 있으므로 위치 4로 이동합니다. 이때 1 칸을 앞으로 점프하면 도착하므로 건전지 사용량이 2 만큼 듭니다.
위의 3가지 경우 거리가 5만큼 떨어져 있는 장소로 가기 위해서 3번째 경우가 건전지 사용량이 가장 적으므로 답은 2가 됩니다.

제한 사항
숫자 N: 1 이상 10억 이하의 자연수
숫자 K: 1 이상의 자연수
입출력 예
N	result
5	2
6	2
5000	5
'''
'''
pseudo code
def solution(n): # n번째 위치가 지정됨. 



'''
import math

def solution(n):  #12를 넣는다고 가정하자.
    count = 0
    while(True):
        if(n%2 != 0):
            n -= 1
            count += 1
        else:
            n /= 2
        if n==0:
            break
    return count


print(solution(5000))

'''
효율성 오류  ㅁㅊ 졸라 어렵게 생각했는데.... 병신이였음
import math

def solution(n):
    lineNum = int(math.log2(n))
    index = n-pow(2,lineNum)


    tempList=[1]
    for j in range(lineNum):
        addList = [i+1 for i in tempList]
        tempList += addList
    return tempList[index]
'''


'''
다른 사람 신기한 풀이

def solution(n):
    return bin(n).count('1')    //이진법 계산 1카운트.

'''