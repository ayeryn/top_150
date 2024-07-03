# 20


def is_valid(s: str) -> bool:
    stack = []
    mapping = {"}": "{", "]": "[", ")": "("}

    for c in s:
        if c in mapping:
            if not stack or stack[-1] != mapping[c]:
                return False  # no matching open parenthesis

            stack.pop()  # pop matching parenthesis
        else:
            stack.append(c)  # push open parenthesis onto stack

    return True if not stack else False  # all parentheses should be matched
