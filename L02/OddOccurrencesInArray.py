def solution(A):
    x = 0
    for n in A:
        x ^= n
    return x


A = list([9, 3, 9, 3, 9, 7, 9, 7, 5,8,7,8,7])
print(solution(A))