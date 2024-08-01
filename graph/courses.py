# 207

from collections import defaultdict


def courses(courses: int, prereq: list[list[int]]) -> bool:
    # Keep track of prereq to course and course_to_prereq maps
    pre_c = defaultdict(list)
    c_pre = defaultdict(list)
    taken = set()

    for a, b in prereq:
        # Construct graphs
        pre_c[b].append(a)
        c_pre[a].append(b)

    def traverse(x):
        taken.add(x)

        for p in pre_c[x]:

            if all([i in taken for i in c_pre[p]]) and p not in taken:
                traverse(p)

    for i in range(courses):
        # Find all classes can be taken
        if i not in c_pre and i not in taken:
            traverse(i)

    return len(taken) == courses
