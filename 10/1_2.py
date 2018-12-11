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
        self.minx = sys.maxsize
        self.miny = sys.maxsize
        self.maxx = -1
        self.maxy = -1
        for p in points:
            x = p.x
            y = p.y
            # Set min coords
            if x < self.minx:
                self.minx = x
            if y < self.miny:
                self.miny = y
            # Set max coords
            if x > self.maxx:
                self.maxx = x
            elif y > self.maxy:
                self.maxy = y

    @property
    def width(self):
        return self.maxx - self.minx

    @property
    def height(self):
        return self.maxy - self.miny

    def __repr__(self):
        return "BoundingBox({}, {}, {}, {})".format(
            self.minx, self.maxx, self.miny, self.maxy
        )


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


def step(points, step_size, min_x, max_x, min_y, max_y):
    remove_points = []
    for point in points:
        point.update(step_size)
        if point.x > max_x or point.x < min_x or point.y > max_y or point.y < min_y:
            remove_points.append(point)

    for remove_point in remove_points:
        points.remove(remove_point)


def draw(points, min_x, max_x, min_y, max_y, time):
    print(time)
    bb = BoundingBox(points)
    for y in range(bb.miny, bb.maxy + 1):
        for x in range(bb.minx, bb.maxx + 1):
            if any(point.x == x and point.y == y for point in points):
                print("#", end="")
            else:
                print(".", end="")

        print()
    print()


points = []


min_x = 0
max_x = 0
min_y = 0
max_y = 0


with open("input.txt") as fh:
    for line in fh:
        x, y, xv, yv = parse_line(line)
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

        points.append(Point(x, y, xv, yv))

# normalize
x_add = abs(min_x)
y_add = abs(min_y)
min_x += x_add
max_x += x_add
min_y += y_add
max_y += y_add

for p in points:
    p.x += x_add
    p.y += y_add

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
    step(points, step_size, min_x, max_x, min_y, max_y)
    if not points:
        keep_simulating = False

    if is_interesting(points):
        draw(points, min_x, max_x, min_y, max_y, time + 1)

    time += step_size
