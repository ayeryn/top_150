# 71


def simplify(path: str) -> str:
    dirs = path.split("/")
    stack = []

    for d in dirs:
        """
        .: current dir - ignore
        ..: previous dir - go back
        ...+: valid dir
        """
        if d == "." or d == "":
            # skip curr dir and empty strings
            continue
        if d == "..":
            # return to prev dir
            if stack:
                stack.pop()
        else:
            # append regular dir to stack
            stack.append(d)

    ans = "/" + "/".join(stack)
    return ans
