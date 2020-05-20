'''
pseudo code

def sol(s):
    string to lower case
    count p
    count s

    num p == num s
        return True
    else
        return False

'''
def solution(s):
    testlist = s.lower()
    pnum, snum = testlist.count("p"), testlist.count('y')

    if pnum == snum:
        return True
    else:
        return False



