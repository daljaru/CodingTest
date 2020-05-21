def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True


def solution(n):
    count = 0
    for i in range(2, n+1):
        if is_prime(i) == True:
            count+=1
    return count


#시간초과
# def solution(n):
#     primeList = [2,3,5,7]
#     if n == 2:
#         return 1
#     elif n == 3:
#         return 2
#     elif n == 5:
#         return 3
#     elif n == 7:
#         return 4
#
#
#     result = [x for x in range(2,n+1) if x%2 != 0 and x%3 != 0 and x%5 != 0 and x% 7 != 0]
#     for num in result:
#         if isDivPrime(num, primeList) is False:#소수 리스트에서 안나눠지면..
#             if isDivCheckNum(max(primeList)+1, num) is False:
#                     primeList.append(num)
#     return len(primeList)
#
# def isDivPrime(num, primeList):
#     for prime in primeList:
#         if num % prime == 0:
#             return True
#     return False
#
# def isDivCheckNum(numOverMaxPrime, num):
#     for checkNum in range(numOverMaxPrime, num):  # 소수리스트에서 가장 큰것부터 num전까지 나눠봄.
#         if num % checkNum == 0:
#             return True
#     return False



'''감동이다..  에라토스테네스의 체를 set으로 풀 수도 있구나....
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
'''



set = {1,2,4,5}
set2 = {4,5}
print(set - set2)