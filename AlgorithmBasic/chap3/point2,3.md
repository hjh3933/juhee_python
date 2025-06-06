### 자료구조에 따른 복잡도

**연결 리스트**

- 리스트: 데이터를 여러 개 저장할 때 사용
- 알고리즘에 따라 리스트보다 더 좋은 자료구조가 있다
- 연결 리스트: 여러 데이터를 저장하지만, 각 요소와 함께 다음 요소의 주소를 저장한다

**삽입과 삭제**

- 리스트의 경우 a값을 list1에 삽입하면 삽입 위치 이후의 데이터를 하나씩 뒤로 움직여야 한다
- 리스트의 삽입 복잡도는 최대 O(n), list1의 요소 개수만큼이 된다
- 연결 리스트의 경우 b값을 list2에 삽입하면 삽입 위치의 앞 요소의 주소를 b값의 주소로 변경, 다음 요소의 주소를 b요소 주소란에 저장한다
- 연결 리스트의 삽입 복잡도는 삽입요소 개수인 O(1)이 된다
- 삭제도 마찬가지로 리스트의 복잡도는 O(n), 연결 리스트의 복잡도는 O(1)이다

**리스트 vs 연결 리스트**

- 읽기의 경우 리스트는 요소 번호를 지정해 읽을 수 있기 때문에 복잡도는 O(1)이다
- 그러나 연결 리스트는 앞 요소부터 주소를 찾아가야 하기 때문에 복잡도는 O(n)이 된다
- 또한, 위치가 특정되지 않은 요소를 삽입, 삭제하려면 O(n)의 처리 시간이 필요하기 때문에 다루는 데이터의 종류와 처리에 맞는 자료구조를 선택해서 사용하는 것이 중요하다

### 알고리즘 복잡도와 문제 복잡도

**복잡도 클래스**

- 소수 구하기의 시간 복잡도와, 에라토스테네스의 체라는 알고리즘의 예시를 통해 시간 복잡도와 알고리즘 복잡도는 구분된다는 점을 알 수 있다
- 복잡도 클래스: 계산의 어려움을 클래스로 구분한 것으로 기본이 시간 복잡도 클래스이다
- O(n), O(n^2)와 같이 지수부분이 정수가 되는 것을 다항식 시간 복잡도라고 하며, 직관적으로 대소에 따라 문제를 분류할 수 있다
- 다항식 시간 복잡도로 풀 수 있는 문제를 P문제라고 한다

**지수 시간 알고리즘**

- 지수 부분에 n이 사용되는 O(2^n)과 같은 것을 지수 시간 알고리즘이라고 하며, n이 조금만 커져도 처리시간이 급증하게 된다
- 배낭 문제
  - 지수 시간 알고리즘의 예시 중 하나이다
  - 담을 수 있는 무게가 한정 된 배낭이 있고, 무게와 가치가 각각 다른 요소들을 지정된 배낭 무게이하로, 최대의 가치를 가지도록 담는 알고리즘이다
  - n개의 물건이 있을 때 총 2^n가지를 체크해야하므로 O(2^n)의 시간복잡도를 가지게 된다

**계승 계산 알고리즘**

- n의 계승, O(n!)의 복잡도를 가지는 알고리즘을 말한다
- `n! = n * (n-1) * (n-2) * ... * 2 * 1`
- 외판원 문제
  - n개의 도시가 있고, 각 도시 간의 거리를 알고 있을 때 모든 도시를 방문하고 첫번째 도시로 돌아오는데 걸리는 최단 경로를 구하는 문제이다
  - 도시가 n개있으면 처음에는 n개의 경로, 그 다음에는 n-1개의 경로로 줄어들면서 O(n!)이라는 처리시간이 필요하게 된다

**P != NP**

- 배낭문제, 외판원 문제 등과 같이 다항식 시간 복잡도 알고리즘으로는 해결이 불가능한 문제를 **NP-난해문제**라고 한다
- NP: Non deterministic Polynomial time, 비결정론적 다항 시간으로 처리할 수 있는 클래스
- 클래스 NP에 대한 효율적인 알고리즘은 현재 존재하지 않으며, NP문제를 다항식 시간으로 푸는 알고리즘은 존재하지 않을 것으로 예측하여 P != NP 예상이라는 수학적 난제로 불리고 있다
