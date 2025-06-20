### 슬라이딩 윈도우

**슬라이딩 윈도우**

- 2개의 포인터로 범위를 지정한 다음, 범위를 유지한 채로 이동하며 문제를 해결하는 알고리즘
- 투 포인터와 매우 유사하고 원리가 간단하다
- 지정된 범위가 하나씩 이동하는 모습이 창문을 밀어서 여는 것과 비슷하여 붙여진 이름

**문제 009**

- 백준 12891
- {'A','C','G','T'}로 이루어진 DNA 문자열이 주어졌을 때 이중 N개의 연결된 문자열을 골라 비밀번호로 만드려고 한다. 비밀번호는 각각 DNA문자들의 개수 조건을 충족해야한다. 생성가능한 비밀번호의 개수를 구하는 문제
- checkSecret: {'A','C','G','T'}의 개수 조건을 충족하는지 알 수 있는 변수, 4가 되면 모든 조건을 만족한다는 의미이다
- checkList, myList: DNA 문자의 조건, DNA문자의 현재 개수를 각각 저장하는 리스트 비교를 통해 checkSecret판단
- myadd, myremove: 함수는 더해지는 문자, 빠지는 문자 c에 대하여 각각 어떤 DNA 문자인지 조건을 판단하고, myList와 checkList를 비교하여 checkSecret을 업데이트하는 작업을 한다
- myadd와 myremove 함수를 실행하고 checkSecret이 4이면 result 개수를 추가하여 결과를 계산한다

```python
def myadd(c):
    global checkList, myList, checkSecret
    if c == "A":
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == "C":
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == "G":
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == "T":
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1
###
for i in range(P, S):
    j = i - P
    myadd(A[i])
    myremove([A[j]])
    if checkSecret == 4:
        result += 1
```

**[실습파일](chap03_4.py)**
