def solution(S, P, Q):
    result = []
    for i, j in zip(P, Q):
        impact_factor = S[i:j + 1]
        if 'A' in impact_factor:
            result.append(1)
        elif 'C' in impact_factor:
            result.append(2)
        elif 'G' in impact_factor:
            result.append(3)
        else:
            result.append(4)
    return result


print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))
