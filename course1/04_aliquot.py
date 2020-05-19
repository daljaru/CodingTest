'''
pseudo code

'''


'''
다른 좋은 풀이

'''

'''
pseudo code



'''
def solution(n):
    aliquot = [x for x in range(1, (n//2)+1) if n%x == 0]
    print(aliquot)
    return sum(aliquot)
    # aliquot = []
    # for i in range(1,(n//2)):
    #     if n % i == 0:
    #         aliquot.append(i)
    #         aliquot.append(n//i)
    # return sum(aliquot)
        


'''
다른 좋은 풀이

'''

print(solution(36))