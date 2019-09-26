def solution(S):
    occurrences = [0] * 26

    for i in range(len(S)):
        occurrences[ord(S[i]) - ord('a')] += 1

    best_char = 'a'
    best_res = 0

    for i in range(25, -1, -1):
        if occurrences[i] >= best_res:
            best_char = chr(ord('a') + i)
            best_res = occurrences[i]

    return best_char


print(solution('hello'))
print(solution('gzacdzd'))
