def solution(A):
    total = sum(A)
    minimum = float('inf')
    left = 0
    for value in A[:-1]:
        left += value
        minimum = min(abs(total - left - left), minimum)
    return minimum


A = [3, 1, 2, 4, 3]
print(solution(A))
