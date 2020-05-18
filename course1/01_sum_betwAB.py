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