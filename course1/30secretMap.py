'''
입출력 예제
매개변수	값
n	5
arr1	[9, 20, 28, 18, 11]
arr2	[30, 1, 21, 17, 28]
출력	["#####","# # #", "### #", "# ##", "#####"]

매개변수	값
n	6
arr1	[46, 33, 33 ,22, 31, 50]
arr2	[27 ,56, 19, 14, 14, 10]
출력	["######", "### #", "## ##", " #### ", " #####", "### # "]


필요한 것 :1 두 배열의 원소인 정수를 이진수화.
9 -> 01001
30 -> 11110
정수의 이진화 알고리즘 필요.


이진화된 두 배열의 같은 인덱스의 원소마다
or 계산.
or계산 방법 알아야함

계산된 이진수를 #과 공백으로 변환. 11011 -> "## ##"
변환 알고리즘.

변환된 것을 리스에 추가.
'''
def trans(binaryStr, transDict):
    result = []
    for i in range(len(binaryStr)):
        result.append(transDict.get(binaryStr[i]))
    return "".join(result)

def solution(n, arr1, arr2):
    transDict ={"1":"#", "0":" "}
    binary = []
    result = []
    for i in range(n):
        binaryStr = []
        binary.append(arr1[i] | arr2[i])
        binary[i] = bin(binary[i])[2:2+n]
        if len(binary[i]) != n:
            for j in range(n - len(binary[i])):
                binaryStr.append("0")
            binaryStr.append(binary[i])
        else:
            binaryStr.append(binary[i])
        temp = trans("".join(binaryStr), transDict)
        result.append(temp)

    return result


print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))


''''
신가한 다른 사람 풀이
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
'''

#100 4
#010 2

#1106
