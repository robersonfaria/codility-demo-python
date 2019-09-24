def solution(A):
    if sorted(A).__eq__(list(range(1, len(A)+1))):
        return 1
    else:
        return 0


print(solution([4, 1, 3, 2]))
print(solution([4, 5, 6, 4, 5, 6]))
# print(solution(list(range(1, 1000000000))))