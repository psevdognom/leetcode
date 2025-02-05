from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isdigit():  # если токен - число, добавляем в стек
                stack.append(int(token))
            else:  # если токен - оператор, выполняем операцию
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(a / b))
            print(stack)
        return int(stack.pop())

if __name__ == '__main__':
    s = Solution()
    expression = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(s.evalRPN(expression))  # 22
