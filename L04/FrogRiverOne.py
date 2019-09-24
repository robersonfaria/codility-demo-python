def solution(X, A):
    B = [-1] * X
    for pos in range(0, len(A)):
        if B[A[pos] - 1] != -1:
            continue
        B[A[pos] - 1] = pos
        X -= 1
        if X == 0:
            return pos
    return -1


print(solution(5, [1]))
print(solution(5, [1, 2, 3, 2, 5, 3]))  # -1
print(solution(5, [1, 2, 1, 2, 1, 2, 3, 1, 4, 5, 4, 1, 3]))  # 9
print(solution(5, [1, 5, 1, 4, 2, 3, 4, 4]))  # 5
print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))  # 6
print(solution(5, [1, 3, 2, 4, 5]))  # 4
print(solution(100000, list(range(1, 100001))))  # 6
