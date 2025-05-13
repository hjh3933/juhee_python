### 다익스트라 알고리즘

**정점에 주목한 최단경로찾기**

- 연결된 정점을 후보로 하여 비용이 가장 적어지는 정점을 선택하는 과정을 반복해 탐색하는 알고리즘
- 변의 값이 음수인 경우 사용이 불가능하지만, 빠른속도(효율적)로 문제를 풀 수 있다
- 비용이 최소인 것만 탐색하므로 그 외에는 탐색할 필요가 없다

**알고리즘 구현하기**

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

**[실습파일](point3_ex.py)**
