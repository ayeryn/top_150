# 68
import math


def text_justification(words: list[str], maxWidth: int) -> list[list[str]]:
    def process_line(line, count, last_line):
        if len(line) == 1:
            # Only word is always left-justified
            return line[0] + " " * (maxWidth - len(line[0]))

        spaces = maxWidth - count
        slots = len(line) - 1
        ans = ""

        if last_line:
            # left aligned
            for i in range(len(line) - 1):
                ans += line[i] + " "
            return ans + line[-1] + (spaces - slots) * " "

        else:
            """
            Since left slots get more spaces when uneven, we can keep getting ceil(spaces_left / slots_left) until slots_left reaches 0
            """
            ls = math.ceil(spaces / slots)

            for i in range(slots):
                ans += line[i] + " " * ls
                spaces -= ls
                slots -= 1
                if slots:  # update ls until slots reaches 0
                    ls = math.ceil(spaces / slots)

            return ans + line[-1]  # append last word to ans

    ans = []
    line = [] # words on one line
    count = 0 # number of characters only
    for w in words:
        if line != "":
            if count + len(line) + len(w) > maxWidth:
                """
                Wrap up current line and start new line when
                - # of characters + 
                - spaces needed if appending current word =
                - len(w)
                is > maxWidth
                """
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
