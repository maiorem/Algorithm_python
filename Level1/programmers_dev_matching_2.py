import datetime 


def solution(p, n) :
    answer=''
    if 'AM' in p :
        p=p.lstrip('AM ')
        temp=datetime.datetime.strptime(p, '%H:%M:%S')
        temp=temp+datetime.timedelta(seconds=n)
    elif 'PM' in p :
        p=p.lstrip('PM ')
        temp=datetime.datetime.strptime(p, '%H:%M:%S')
        temp=temp+datetime.timedelta(hours=12, seconds=n)
    answer=datetime.datetime.strftime(temp, '%H:%M:%S')
    return answer


print(solution('PM 11:59:59', 10))
