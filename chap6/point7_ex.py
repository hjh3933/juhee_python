# 역폴란드 표기법


def calc(expression):
    stack = []

    # 공백으로 요소를 구분하여 리스트의 첫번째 요소부터 하나씩 사용
    for i in expression.split(" "):
        print(stack)

        # 사칙연산의 경우 계산값을 stack에 쌓기
        if i == "+":
            # 후입선출이므로 순서에 주의
            b, a = stack.pop(), stack.pop()
            stack.append(a + b)
        elif i == "-":
            b, a = stack.pop(), stack.pop()
            stack.append(a - b)
        elif i == "*":
            b, a = stack.pop(), stack.pop()
            stack.append(a * b)
        elif i == "/":
            b, a = stack.pop(), stack.pop()
            stack.append(a // b)
        # 숫자인 경우 stack에 쌓기
        else:
            stack.append(int(i))

    return stack[0]


print(calc("4 6 2 + * 3 1 - 5 * -"))
