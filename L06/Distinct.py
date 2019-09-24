def solution(A):
    return len(set(A))


print(solution([2, 1, 1, 2, 3, 1]))
print(solution(list(range(0, 100000))))
print(solution(list(range(-1000000, 1000000))))
