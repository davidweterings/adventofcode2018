import sys

N = M = 1000
matrix = {(x, y): 0 for x in range(N) for y in range(M)}

occupied = set()
all_fabric = []
with open("input.txt") as fh:
    for line in fh:
        if line:
            fabric_id, remainder = line.split("@")
            fabric_id = fabric_id.split("#")[1]
            coords, dimensions = remainder.split(":")
            start_x, start_y = map(int, coords.split(","))
            x_length, y_length = map(int, dimensions.split("x"))
            for i in range(x_length):
                x = start_x + i
                for j in range(y_length):
                    y = start_y + j
                    if not matrix[(x, y)]:
                        matrix[(x, y)] = fabric_id
                    else:
                        matrix[(x, y)] = "X"

with open("input.txt") as fh:
    for line in fh:
        if line:
            fabric_id, remainder = line.split("@")
            fabric_id = fabric_id.split("#")[1]
            coords, dimensions = remainder.split(":")
            start_x, start_y = map(int, coords.split(","))
            x_length, y_length = map(int, dimensions.split("x"))
            all_match = 0
            for i in range(x_length):
                x = start_x + i
                for j in range(y_length):
                    y = start_y + j
                    if matrix[(x, y)] == fabric_id:
                        all_match += 1
            if all_match == x_length * y_length:
                print(fabric_id)
                sys.exit(0)
