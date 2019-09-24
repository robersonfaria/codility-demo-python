def solution(A):
    L = len(A)
    E = (L + 1) * (L + 2) // 2
    return E - sum(A)


A = [2, 3, 5, 1, 4, 6]
print(solution(A))
