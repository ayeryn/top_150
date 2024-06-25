# 68


def text_justification(words: list[str], maxWidth: int) -> list[list[str]]:
    def process_line(line, count, last_line):
        if len(line) == 1:
            return line[0] + " " * (maxWidth - len(line[0]))

        spaces = maxWidth - count
        ans = ""
        if last_line:
            # left aligned
            for i in range(len(line) - 1):
                ans += line[i] + " "
            return ans + line[-1] + (spaces - (len(line) - 1)) * " "

        else:
            s = spaces // (len(line) - 1)
            ans = line[0] + " " * (s + spaces % (len(line) - 1))

            for i in range(1, len(line) - 1):
                ans += line[i] + s * " "

            return ans + line[-1]

    ans = []
    line = []
    count = 0
    for w in words:
        # print(f"w = {w}, line = {line}, c = {count}, op = {count + len(line) + len(w) - 1}")
        if line != "":
            if count + len(line) + len(w) > maxWidth:
                # wrap up current line and start nl
                ans.append(process_line(line, count, False))
                line = [w]
                count = len(w)
            else:
                line.append(w)
                count += len(w)
        else:
            line.append(w)
            count += len(w)
    ans.append(process_line(line, count, True))
    return ans
