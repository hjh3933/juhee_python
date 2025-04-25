# check1
# 10층 건물에서 1층에서 10층까지 이동할 때, 정지하는 층의 조합을 구하는 문제
case = []
goal = 10


def elevator(current, path):
    if current == goal:
        case.append(path[:])
        return
    for next_floor in range(current + 1, 11):
        path.append(next_floor)
        elevator(next_floor, path)
        path.pop()


elevator(1, [1])
print(len(case))
