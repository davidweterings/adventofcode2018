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

matrix = {(x, y): "." for x in range(max_x) for y in range(max_y)}

for idx, point in enumerate(points):
    matrix[(point[0], point[1])] = idx


def manhattan_distance(x, y, ox, oy):
    return abs(x - ox) + abs(y - oy)


for matrix_point in matrix.keys():
    x, y = matrix_point[0], matrix_point[1]
    #if (x,y) in points:
        #continue
    dist = sys.maxsize
    found_idx = None
    if sum(manhattan_distance(x, y, point[0], point[1]) for point in points) < 10000:
        matrix[matrix_point] = '#'


total=0
for x in range(max_x):
    for y in range(max_y):
        if matrix[(x,y)] == '#':
            total += 1


print(total)
