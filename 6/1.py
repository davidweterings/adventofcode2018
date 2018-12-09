import sys

points = []

max_x = 0
max_y = 0
with open("input.txt") as fh:
    for index, line in enumerate(fh):
        if line:
            x, y = map(int, line.split(","))
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
            points.append((x, y))

max_x+=1
max_y+=1

matrix = {(x, y): "" for x in range(max_x) for y in range(max_y)}

for idx, point in enumerate(points):
    matrix[(point[0], point[1])] = idx


def manhattan_distance(x, y, ox, oy):
    return abs(x - ox) + abs(y - oy)


for matrix_point in matrix.keys():
    x, y = matrix_point[0], matrix_point[1]
    if (x,y) in points:
        continue
    dist = sys.maxsize
    found_idx = None
    for idx, point in enumerate(points):
        mh = manhattan_distance(x, y, point[0], point[1])
        if mh < dist:
            dist = mh
            found_idx = idx
        elif mh == dist and found_idx != None:
            found_idx = '.'

    matrix[matrix_point] = found_idx


def is_enclosed(x, y):
    try:
        matrix[(x+1, y)]
        matrix[(x, y+1)]
        matrix[(x+1, y+1)]
        matrix[(x-1, y-1)]
        matrix[(x-1, y)]
        matrix[(x, y-1)]
        matrix[(x-1, y+1)]
        matrix[(x+1, y-1)]
        return True
    except KeyError:
        return False

exclude = set()
for idx, _ in enumerate(points):
    for x in range(max_x):
        for y in range(max_y):
            if not is_enclosed(x, y):
                exclude.add(matrix[(x,y)])

print("Excluding: ", exclude)
total_enclosed = 0
for idx, _ in enumerate(points):
    if idx in exclude:
        continue
    enclosed = 0
    for x in range(max_x):
        for y in range(max_y):
            if matrix[(x,y)] == idx:
                enclosed += 1
    if enclosed > total_enclosed:
        total_enclosed = enclosed


print(total_enclosed)
sys.exit(0)
for x in range(max_x):
    for y in range(max_y):
        print(matrix[(x,y)], end="") 
    print()
