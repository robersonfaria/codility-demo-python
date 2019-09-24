def solution(A):
    if len(A) >= 3:
        A.sort()
        for index in range(0, len(A) - 2):
            if A[index] + A[index + 1] > A[index + 2]:
                return 1
    return 0


print(solution([10, 2, 5, 1, 8, 20]))
print(solution(list(range(-2147483648, 2147483647))))
