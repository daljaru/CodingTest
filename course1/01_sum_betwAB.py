'''
pseudo code
def solution(a, b):
    result = formula_sum_Between_a_and_b(a, b)
    return result

of

def solution(a, b):
    for i in a와 b사이의 길이만큼:
        total += a 부터 하나씩 올려서 더하기

    return total
'''


def solution(a, b):
    answer = (abs(a-b)+1)*(a+b)/2
    return answer


if __name__ == '__main__':
    answer = solution(5, 3)
    print(answer)



# 다른 좋은 풀이들...  그냥 sum을 쓰면 되는 것이였다.
 def adder(a, b):
    # 함수를 완성하세요
    if a > b: a, b = b, a

    return sum(range(a,b+1))   


def adder(a, b):
    # 함수를 완성하세요
    return sum(range(min(a,b),max(a,b)+1))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( adder(3, 5))