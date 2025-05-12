### 벨만포드알고리즘

**변의 가중치**

- 지점과 변으로 이루어진 지도에서 최단거리를 찾는 문제의 경우, 변의 가중치가 부여되어있을 수 있다(실생활 속 거리 개념처럼)
- BFS로는 이러한 문제를 해결하기 어렵다
- 벨만포드 알고리즘은 변의 가중치를 이용해 지점별 최단거리를 갱신하는 방식으로 구현된다

**초기 설정과 갱신의 원리**

- 시작점은 0으로 설정하고 나머지 지점은 무한대를 설정하여, 대소비교를 통해 최단거리로 갱신하도록 한다
- 파이썬의 `float('inf')`를 통해 설정할 수 있다
- 갱신
  - 모든 변 중의 하나를 선택한다
  - 변을 연결하는 A, B 지점에 대하여 `A + 변의 비용` < `B` 인 경우 더 작은 값인 `A + 변의 비용`을 정점 B의 값으로 갱신하게 된다
  - 같은 과정을 모든 **변**에 대하여 진행한다
  - 모든 정점에 대하여 갱신이 불가능해지면 코드를 종료한다

**프로그램 구현하기**

- bellman_ford: 함수는 변 리스트와 정점의 개수를 매개변수로 받고, 정점별 이동값이 저장된 dist를 리턴한다
- dist: 시작점을 제외하고 무한대로 초기화하고, 최단거리를 갱신한 값을 저장한다
- changed: 갱신 여부를 저장한다, while문의 조건으로 모든 정점에 대하여 갱신이 불가능해지면 while문이 종료된다
- edges, edge: [A,B,A-B값]으로 구성된 edge로 이루어진 리스트 edges

```python
def bellman_ford(edges, num_v):
    dist = [float("inf") for i in range(num_v)]
    dist[0] = 0
    changed = True

    while changed:
        changed = False
        for edge in edges:
            if dist[edge[1]] > dist[edge[0]] + edge[2]:
                dist[edge[1]] = dist[edge[0]] + edge[2]
                changed = True

    return dist
```

**[실습파일](point2_ex.py)**
