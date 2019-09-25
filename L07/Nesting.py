def solution(S):
    if S and (len(S) % 2 != 0 or S[0] == ')'):
        return 0

    control = []
    for value in list(S):
        if value == '(':
            control.append("(")
        elif len(control) > 0:
            control.pop()
        else:
            return 0

    if len(control) == 0:
        return 1
    return 0


print(solution(""))
print(solution("(()(())())"))
print(solution("())"))
print(solution(")())"))
print(solution("()))"))
import random
r = [random.choice('()') for _ in range(1000000)]
print(solution(r))
