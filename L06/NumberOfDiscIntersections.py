def solution(A):
    count = 0
    for center, radius in enumerate(A):
        if count > 10000000:
            return -1
        circ1 = set(range(center - radius, center + radius + 1))
        for c, r in enumerate(A):
            if center < c:
                if len(circ1.intersection(set(range(c - r, c + r + 1)))) > 0:
                    count += 1
    return count


print(solution([1, 5, 2, 1, 4, 0]))
# print(solution(range(1, 10000000)))
