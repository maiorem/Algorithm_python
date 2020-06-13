
def solution(a, b) :
    n = 0
    before_sum = 0
    while True :
        sum = a + n
        n = n + 1
        before_sum = sum
        sum = sum + before_sum
        if sum == b :
            break
    answer = sum
    if a == b :
        answer = a
    return answer

print(solution(2,5))