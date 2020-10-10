from collections import Counter 

def solution(votes, k):
    answer = ''
    vote_result=Counter(votes)
    sorted(vote_result)
    
    return answer

print(solution(["AVANT", "PRIDO", "SONATE", "RAIN", "MONSTER", "GRAND", "SONATE", "AVANT", "SONATE", "RAIN", "MONSTER", "GRAND", "SONATE", "SOULFUL", "AVANT", "SANTA"], 2))