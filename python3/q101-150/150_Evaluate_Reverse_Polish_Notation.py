from typing import List
import operator


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation = {
            '+': lambda y, x: x + y,
            '-': lambda y, x: x - y,
            '*': lambda y, x: x * y,
            '/': lambda y, x: int(operator.truediv(x, y))
        }

        if not tokens:
            return 0

        stack = []

        for token in tokens:
            if token in operation:
                stack.append(operation[token](stack.pop(), stack.pop()))
            else:
                stack.append(int(token))

        return stack[0]
