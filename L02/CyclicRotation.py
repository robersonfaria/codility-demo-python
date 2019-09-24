def solution(A, K):
    new = []
    for i in range(len(A)):
        new.append(A[(i - K) % len(A)])
    return new


A = [3, 8, 9, 7, 6]
K = 3
print(solution(A, K))
A = [0, 0, 0]
K = 1
print(solution(A, K))
A = [1, 2, 3, 4]
K = 4
print(solution(A, K))
