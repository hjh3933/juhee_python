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

# 삽입정렬
data1 = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

for i in range(1, len(data1)):
    # 임시공간에 저장
    temp = data1[i]
    # 요소 앞에서부터 비교 시작
    j = i - 1
    while (j >= 0) and (data1[j] > temp):
        # 한칸 뒤로 옮김
        data1[j + 1] = data1[j]
        # 앞의 요소에 대하여 반복문 실행
        j -= 1
    # while문 종료 후 임시값을 앞으로 저장
    data1[j + 1] = temp

print(data1)
