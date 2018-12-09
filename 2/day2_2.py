import sys

from collections import Counter

box_ids = []

with open("input.txt") as fh:
    for line in fh:
        if line:
            box_ids.append(line)


def edit_distance(s1, s2):
    m = len(s1) + 1
    n = len(s2) + 1

    tbl = {}
    for i in range(m):
        tbl[i, 0] = i
    for j in range(n):
        tbl[0, j] = j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            tbl[i, j] = min(
                tbl[i, j - 1] + 1, tbl[i - 1, j] + 1, tbl[i - 1, j - 1] + cost
            )

    return tbl[i, j]



for box_id in box_ids:
    for other_box_id in box_ids:
        if box_id == other_box_id:
            continue
        distance = edit_distance(box_id, other_box_id)
        if distance == 1:
            solution = []
            for i in range(len(box_id)):
                if box_id[i] == other_box_id[i]:
                    solution.append(box_id[i])

            print(''.join(solution))
            sys.exit(0)
