data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
min = 0

for i in range(1, len(data)):
    if data[min] > data[i]:
        min = i

print("최솟값: ", data[min])  # 위치(인덱스)는 min(3)

# 선택정렬

for i in range(0, len(data)):
    min = i
    for j in range(min + 1, len(data)):
        if data[min] > data[j]:
            min = j  # 계속해서 갱신
    # for문 종료 후 최종 갱신값과 교환
    data[i], data[min] = data[min], data[i]

print(data)
