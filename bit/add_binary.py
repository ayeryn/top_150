# 67
def add_binary(a: str, b: str) -> str:
    if a == b == "0":
        return a

    # ans is at most 1 bit longer than the longer str
    ans = ["" for _ in range(max(len(a), len(b)) + 1)]
    carry = False
    i = -1  # Traverse backwards

    while -i <= len(a) and -i <= len(b):
        if a[i] == "0" and b[i] == "0":
            if carry:
                ans[i] = "1"
            else:
                ans[i] = "0"
            carry = False
        elif a[i] == "1" and b[i] == "1":
            if carry:
                ans[i] = "1"
            else:
                ans[i] = "0"
            carry = True
        else:
            if carry:
                ans[i] = "0"
            else:
                ans[i] = "1"
        i -= 1

    # Deal with the longer str
    # If equal len then we are done
    if len(a) > len(b):
        while -i <= len(a):
            if a[i] == "1":
                ans[i] = "0" if carry else "1"
            else:
                if carry:
                    ans[i] = "1"
                    carry = False
                else:
                    ans[i] = "0"
            i -= 1
    elif len(b) > len(a):
        while -i <= len(b):
            if b[i] == "1":
                ans[i] = "0" if carry else "1"
            else:
                if carry:
                    ans[i] = "1"
                    carry = False
                else:
                    ans[i] = "0"
            i -= 1

    if carry:  # Take care of leading "1"
        ans[0] = "1"

    return "".join(ans) if ans[0] == "1" else "".join(ans[1:])
