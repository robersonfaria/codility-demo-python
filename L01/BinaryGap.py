def solution(N):
    return len(max(format(N, 'b').strip('0').split('1')))


print(solution(9)) #2
print(solution(529)) #4 3
print(solution(20)) #1
print(solution(15)) #0
print(solution(32)) #null
print(solution(2147483647)) #null
