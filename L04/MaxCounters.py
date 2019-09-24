def solution(N, A):
    new = [0] * N
    for X in A:
        if 1 <= X <= N:
            new[X - 1] += 1
        else:
            new = [max(new)] * N
    return new


print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
print(solution(5, range(1, 100000)))
