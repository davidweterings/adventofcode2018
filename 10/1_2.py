import re
import sys
from collections import Counter


class BoundingBox:
    """
    A 2D bounding box
    """

    def __init__(self, points):
        if len(points) == 0:
            raise ValueError("Can't compute bounding box of empty list")
        self.min_x = sys.maxsize
        self.min_y = sys.maxsize
        self.max_x = -1
        self.max_y = -1
        for p in points:
            x = p.x
            y = p.y
            if x < self.min_x:
                self.min_x = x
            if y < self.min_y:
                self.min_y = y
            if x > self.max_x:
                self.max_x = x
            elif y > self.max_y:
                self.max_y = y

    @property
    def width(self):
        return self.max_x - self.min_x

    @property
    def height(self):
        return self.max_y - self.min_y

    def __repr__(self):
        return "BoundingBox({}, {}, {}, {})".format(
            self.min_x, self.max_x, self.min_y, self.max_y
        )

    def contains(self, point):
    	return self.min_x <= point.x <= self.max_x and self.min_y <= point.y <= self.max_y


class Point:
    def __init__(self, x, y, xv, yv):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv

    def update(self, step_size):
        self.x += self.xv * step_size
        self.y += self.yv * step_size

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Point):
            return (
                self.x == other.x
                and self.y == other.y
                and self.xv == other.xv
                and self.yv == other.yv
            )
        return NotImplemented

    def __str__(self):
        return f"{self.x},{self.y} - {self.xv}, {self.yv}"

    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.xv}, {self.yv})"


def parse_line(line):
    parsed = list(map(int, re.findall(r"[-\d]+", line)))
    return parsed[0], parsed[1], parsed[2], parsed[3]


def step(points, step_size, grid_bb):
    remove_points = []
    for point in points:
        point.update(step_size)
        if not grid_bb.contains(point):
            remove_points.append(point)

    for remove_point in remove_points:
        points.remove(remove_point)


def draw(points, time):
    print(time)
    bb = BoundingBox(points)
    for y in range(bb.min_y, bb.max_y + 1):
        for x in range(bb.min_x, bb.max_x + 1):
            if any(point.x == x and point.y == y for point in points):
                print("#", end="")
            else:
                print(".", end="")

        print()
    print()


points = []

with open("input.txt") as fh:
    for line in fh:
        x, y, xv, yv = parse_line(line)
        points.append(Point(x, y, xv, yv))

grid_bb = BoundingBox(points)

# normalize
x_add = abs(grid_bb.min_x)
y_add = abs(grid_bb.min_y)

for p in points:
    p.x += x_add
    p.y += y_add

grid_bb = BoundingBox(points)

time = 0
step_size = 1
keep_simulating = True


def is_interesting(points):
    if points and len(points) > 10:
        bb = BoundingBox(points)
        if bb.width < 100:
            x_counter = Counter()
            for point in points:
                x_counter.update(str(point.x))
            total_x_same = sum(0 if total < 6 else 1 for total in x_counter.values())
            if total_x_same > 3:
                return True

    return False


while keep_simulating:
    step(points, step_size, grid_bb)
    if not points:
        keep_simulating = False

    if is_interesting(points):
        draw(points, time + 1)

    time += step_size
