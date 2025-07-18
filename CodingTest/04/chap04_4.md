### 퀵정렬

**퀵 정렬의 핵심 이론**

- 기준값(pivot)을 선정해 해당 값보다 작은 데이터와 큰 데이터로 분류하는 것을 반복하여 정렬하는 알고리즘
- 평균 시간 복잡도는 O(nlogn)이지만 최악의 경우 O(n^2)이 된다
- 정렬 과정
  - pivot을 설정(start, end 이동을 위해 주로 맨 끝에 위치시킴)
  - start < pivot: start를 오른쪽으로 +1 칸 이동
  - end > pivot: end를 왼쪽으로 -1 칸 이동
  - start > pivot && end < pivot: start와 end를 swap 각각 오른쪽, 왼쪽 한칸 이동
  - start와 end가 만날 때까지 반복
  - 만난 지점과 pivot을 비교하여 위치시키고 분리 집합에서 다시 pivot을 선정
  - 분리 집합이 1개 이하가 될 때까지 반복
- 재귀함수 형태로 구현된다

**문제 019**

- 백준 11004번
- N개의 수가 주어진다. 이를 오름차순 정렬했을 때 k번째에 있는 수를 구하는 프로그램을 작성하시오
- 첫번째 줄에 N k, 두번째 줄에 N개의 정수가 a1 a2 a3 ... 주어진다
- 퀵정렬을 사용하여 중간위치를 피벗으로 설정한 다음 맨 앞의 값과 swap 한다 -> i, j 이동을 편하게 하기 위함
-

```python
def quickSort(S, E, K):
    global A
    if S < E:
        pivot = partition(S, E)
        if pivot == K:
            return
        elif K < pivot:
            quickSort(S, pivot - 1, K)
        else:
            quickSort(pivot + 1, E, K)
```

**[실습파일](chap04_4.py)**
