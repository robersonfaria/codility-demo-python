def solution(A, B):
    stack = []
    for i in range(len(A)):
        live_fish = i
        while B[live_fish] == 0 and stack and B[stack[-1]] == 1:
            other_fish = stack.pop()
            if A[other_fish] > A[live_fish]:
                live_fish = other_fish
        stack.append(live_fish)
    return len(stack)


print(solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))
print(solution([4, 3, 2, 1, 5], [1, 0, 0, 0, 0]))
print(solution([4, 3, 2, 1, 5], [1, 0, 0, 0, 1]))
