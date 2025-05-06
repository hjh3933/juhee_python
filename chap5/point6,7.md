### 병합정렬

**병합정렬이란**

- 리스트를 반복해서 둘로 분할하고, 뿔뿔이 흩어진 상태에서 리스트를 병합하는 방법
- 병합하는 과정에서 첫번째 요소들끼리 값의 대소를 비교하여 정렬하도록 한다
- 두 리스트를 병합하는 과정의 복잡도는 `O(n)`, 단계수를 고려하면 log2N으로 전체 복잡도는 `O(nlogn)`이 된다

**병합정렬 구현**

- `merge_sort(data)`: 리스트 요소가 1개가 될때까지 재귀를 통해 요소를 분할한다, 이후 merge함수를 통해 각 요소가 병합된 리스트를 반환한다(return)
- `merge(left, right)`: result 변수에 병합된 리스트를 담아 리턴한다, 두 리스트의 첫번째 요소부터 대소를 비교하여 오름차순으로 리스트에 저장한다
- `extend()`: 리스트에 여러 요소를 풀어서 추가

```python
data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]


def merge_sort(data):
    if len(data) <= 1:
        return data
    # 2개 이상의 데이터를 가진 리스트이면 분할함
    mid = len(data) // 2

    # 재귀분할
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    # 병합
    return merge(left, right)


def merge(left, right):
    result = []  # 병합한 리스트를 담을 곳
    i, j = 0, 0  # 두 리스트의 인덱스를 각각 관리, 왼쪽과 오른쪽 리스트라고 생각
    # 인덱스이므로 각각 리스트의 길이보다 작은 조건 부여 -> 리스트가 비워지면 종료
    while (i < len(left)) and (j < len(right)):
        # 대소를 비교하여 더 작은 요소를 result에 추가
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 요소에 대한 처리
    if i < len(left):
        result.extend(left[i:])
    if j < len(right):
        result.extend(right[j:])


print(merge_sort(data))
```

**[실습파일](point6,7_ex.py)**
