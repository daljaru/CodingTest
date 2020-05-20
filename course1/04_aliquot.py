'''
pseudo code
for in range(half length):
    if n // i == 0:
        appendlist...

    return sumoflist
'''

def solution(n):
    aliquot = [n//x for x in range(1, (n//2)+1) if n%x == 0]
    aliquot.append(1)
    return sum(aliquot)
    # aliquot = []
    # for i in range(1,(n//2)):
    #     if n % i == 0:
    #         aliquot.append(i)
    #         aliquot.append(n//i)
    # return sum(aliquot)

'''
다른 좋은 풀이
def sumDivisor(num):
    return sum([i for i in range(1,num+1) if num%i==0])
'''

print(solution(12))