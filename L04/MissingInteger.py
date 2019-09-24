import random


def solution(A):
    return min(set(range(1, len(A) + 2)).difference(set(A)))


print(solution([1, 3, 6, 4, 1, 2]))  # 5
print(solution([1, 2, 3]))  # 4
print(solution([-1, -3]))  # 1
print(solution(range(1, 100000)))  # 1
r = list(range(1, 100000))
random.shuffle(r)
print(solution(r))  # 1
