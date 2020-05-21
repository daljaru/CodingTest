'''
문제분석

월일 구하기
calenar 모듈의 weekday메소드 사용
'''
'''
pseudo code

day=[...]
return day[calendar.weekday(2016, x, y)]
'''
import calendar

def solution(a, b):
    day=["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    return day[calendar.weekday(2016, a, b)]


print(solution(5,24))