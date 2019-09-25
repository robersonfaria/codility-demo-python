def solution(A):
    days = len(A)
    if days < 2:
        return 0
    max_price = A[days - 1]
    max_profit = 0
    for index in range(days - 2, -1, -1):
        max_profit = max(max_profit, max_price - A[index])
        max_price = max(A[index], max_price)
    return max_profit


# def solution(A):
#     max = 0
#     min = A[0]
#     if len(A) < 2:
#         return 0
#     for val in A:
#         if val > max:
#             max = val
#         if val < min:
#             min = val
#             if max > min:
#                 max = min
#     if min < max:
#         return max - min
#     else:
#         return 0


print(solution([23171, 21011, 21123, 21366, 21013, 21367]))
print(solution([5, 1, 8, 3, 9]))
print(solution([1, 8, 3, 2]))
print(solution(range(1, 400000)))
print(solution(list(range(1, 100)) + list(range(2, 200))))
print(solution([0, 200000]))
