sched = [
    (6, 8),
    (6, 12),
    (6, 7),
    (7, 8),
    (7, 10),
    (8, 9),
    (8, 10),
    (9, 12),
    (9, 10),
    (10, 11),
    (10, 12),
    (11, 12),
]

##### 각주와 같이 보기 #####


def bestTimeToParty(schedule):
    # 첫번째 튜플값으로 초기화
    start = sched[0][0]
    end = sched[0][1]
    # 전체 리스트를 돌면서 가장 빠른 입장시간과 가장 마지막 퇴장시간을 저장
    for c in schedule:
        start = min(c[0], start)
        end = max(c[1], end)
    # 시간별 참석자 연예인 수를 저장하는 count 리스트를 별도의 함수로 받아옴
    count = celebrityDensity(schedule, start, end)
    maxCount = 0
    # 최소, 최대 시간 범위의 count 리스트값 중 가장 큰 값을 찾아 maxCount에 저장
    for i in range(start, end + 1):
        if count[i] > maxCount:
            # 함수를 활용하는 방법
            # maxCount = max(count[start:end+1])
            # time = count.index(maxCount)
            maxCount = count[i]
            time = i
    # 해당 시간과 연예인 수에 대한 정보를 담은 문장을 출력
    print(
        "Best time to attend the party is at",
        time,
        "o'clock",
        ":",
        maxCount,
        "celebrities will be attending!",
    )


def celebrityDensity(sched, start, end):
    # 길이가 end+1인 count 리스트 생성하고 모두 0으로 초기화
    count = [0] * (end + 1)
    # for문을 통해 count리스트의 값을 0으로 초기화(명시적으로 초기화하는것 위에서 이미 0으로 초기화되어있긴함)
    for i in range(start, end + 1):
        count[i] = 0
        # sched 리스트의 입장시간이 i보다 빠르고 퇴장시간이 i보다 느리면 count[i]에 +1을 하여 참석중인 연예인 수를 추가함
        for c in sched:
            if c[0] <= i and c[1] > i:
                count[i] += 1
    return count


bestTimeToParty(sched)

##### 더 간결하게 수정해보기 #####
