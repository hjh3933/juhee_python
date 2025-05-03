import queue

# 스택 구현
stack = []

stack.append(2)
stack.append(3)
stack.append(5)

temp = stack.pop()
print(temp)  # 마지막 입력 요소인 5 출력

stack.append(4)
temp = stack.pop()
print(temp)  # 마지막 입력 요소인 4 출력

# 큐 구현
q = queue.Queue()
q.put(2)
q.put(3)
q.put(5)

temp = q.get()
print(temp)  # 첫번째 입력 요소인 2 출력
