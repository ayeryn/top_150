# 150
from math import *


def evalRPN(tokens: list[str]) -> int:
    stack = []

    for token in tokens:
        # Calculate as we go
        if token in "+-*/":
            op2 = stack.pop()
            op1 = stack.pop()
            if token == "+":
                stack.append(op1 + op2)
            elif token == "-":
                stack.append(op1 - op2)
            elif token == "*":
                stack.append(op1 * op2)
            else:
                res = op1 / op2
                if res >= 0:
                    stack.append(floor(res))
                else:
                    stack.append(ceil(res))

        else:
            stack.append(int(token))

    # There should be 1 token left in stack, which is the result of the final operation
    return stack[-1]
