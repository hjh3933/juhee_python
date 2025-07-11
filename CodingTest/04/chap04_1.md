### 버블정렬

**정렬 알고리즘**

- 버블, 선택, 삽입, 퀵, 병합, 기수 알고리즘 등을 다룬다
- 버블정렬이란, 두 인접한 데이터의 크기를 비교하여 swap 연산을 반복하는 방식으로 정렬하는 방법이다
- O(n^2)의 시간복잡도를 가지기 때문에 다소 오래걸리는 편이다
- 파이썬에서는 sort()를 통해 간단히 정렬이 가능하지만 문제 풀이에서는 버블 정렬을 직접 구현했다
- 특정 루프에서 swap 연산이 한번도 발생하지 않았다면 그 영역 뒤에 있는 데이터가 모두 정렬됐다는 뜻이므로 프로세스를 종료한다

**문제 015**

- 백준 2750
- N개의 수가 중복없이 주어졌을 때 오름차순 정렬한 결과를 N개의 줄에 순서대로 출력하시오
- 이중 for문의 형태로 전체 반복문은 N-1 회 실행된다(수를 두개씩 비교하기 때문에 맨 마지막 요소는 앞요소랑 비교되면 끝)
- 내부 반복문은 N-1-i 번 실행된다(N-1번에서 맨 뒤 요소부터 정렬되므로 i씩 빼면서 반복하는 것)
- 왼쪽값(j)이 오른쪽값(j+1)보다 크면 위치를 변경한다

```python
for i in range(N - 1):
    for j in range(N - 1 - i):
        if A[j] > A[j + 1]:
            temp = A[j]
            A[j] = A[j + 1]
            A[j + 1] = temp
```

**문제 016**

- 백준 1377번
- 버블정렬을 통해 N개의 수를 정렬할 때, 정렬하기 위해 필요한 for문의 실행 횟수를 구하는 문제
- 실제로 버블정렬을 사용하면 제한시간을 초과하기 때문에 다른 방식으로 구해야한다
- 파이썬의 내장함수 sort()를 사용하여 구할 수 있다
- 버블정렬의 원리 이해하기
  - 버블정렬의 swap연산에서 특정한 수는 for문 1번당 1칸 이동하게 된다
  - swap 연산이 한번도 일어나지 않으면 정렬된 것으로 이해할 수 있다
  - 정렬전 인덱스와 정렬후 인덱스의 차이를 비교하여 그 최댓값이 for문의 실행횟수가 된다
  - 정렬이 일어나지 않는 마지막 for문도 함께 세야하기 때문에 위의 최댓값 +1을 통해 구할 수 있다

```python
sorted_A = sorted(A)

for i in range(N):
    if sorted_A[i][1] - i > Max:
        Max = sorted_A[i][1] - i
```

**[실습파일](chap04_1.py)**
