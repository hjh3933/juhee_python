### 다익스트라 알고리즘

**정점에 주목한 최단경로찾기**

- 연결된 정점을 후보로 하여 비용이 가장 적어지는 정점을 선택하는 과정을 반복해 탐색하는 알고리즘
- 변의 값이 음수인 경우 사용이 불가능하지만, 빠른속도(효율적)로 문제를 풀 수 있다
- 비용이 최소인 것만 탐색하므로 그 외에는 탐색할 필요가 없다

**알고리즘 구현하기**

- dist: 정점별 비용을 저장, 최종 리턴값, 처음에는 무한대값을 저장함
- q: 정점 리스트
- 가장 작은 정점 q[0]을 r에 대입하고, dist[q[0]] 보다 작은 dist[n]이 있으면 r을 갱신한다
- pop을 통해 가장 비용이 작은 정점을 꺼내서 u에 대입한다
- edges[u] = u정점과 연결된 [끝점, 비용][][]을 하나씩 꺼내서 정점까지의 비용을 갱신할 수 있으면 갱신한다

```python
def dijkstra(edges, num_v):
    dist = [float("inf")] * num_v
    dist[0] = 0
    q = [i for i in range(num_v)]

    while len(q) > 0:
        r = q[0]
        for i in q:
            if dist[i] < dist[r]:
                r = i

        u = q.pop(q.index(r))
        for i in edges[u]:
            if dist[i[0]] > dist[u] + i[1]:
                dist[i[0]] = dist[u] + i[1]

    return dist
```

**[실습파일](point3_ex.py)**
