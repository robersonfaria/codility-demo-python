# Given time in seconds return in the following format <<hours>> h <<minutes>> m <<seconds>> s

def solution(T):
    hour = str(T // 3600)
    minute = str((T % 3600) // 60)
    seconds = str((T % 3600) % 60)
    return hour + "h" + minute + "m" + seconds + "s"


print(solution(7500));
print(solution(83643));
print(solution(86399));
