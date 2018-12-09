from collections import defaultdict
import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)

lines = []
with open("input.txt") as fh:
    for line in fh:
        if line:
            lines.append(line)

"""
[1518-02-17 23:56] Guard #2281 begins shift

[1518-02-18 00:31] falls asleep

[1518-02-18 00:54] wakes up

[1518-02-19 00:00] Guard #1873 begins shift

[1518-02-19 00:12] falls asleep
"""


def get_guard(line) -> str:
    return int(line.split(" ")[3][1:])


def parse_time(line):
    pieces = line.split(" ")
    date_pieces = pieces[0].split("-")
    date = f"{date_pieces[1]}-{date_pieces[2]}"

    time = int(pieces[1][0:-1].split(":")[1])

    return date, time


lines = sorted(lines)
last_guard = None
start = None
asleep_per_guard = {}
asleep_per_guard_per_minute = {}

for line in lines:
    print(line)
    if "Guard" in line:
        last_guard = get_guard(line)
        # pp.pprint(asleep_per_guard_per_minute)
        print("Guard change!!!!")
    if "asleep" in line:
        start_date, start_time = parse_time(line)
    if "up" in line:
        end_date, end_time = parse_time(line)
        if last_guard not in asleep_per_guard:
            asleep_per_guard[last_guard] = 0
            asleep_per_guard_per_minute[last_guard] = {}

        asleep_time = end_time - start_time
        print("Guard asleep for: ", asleep_time)
        asleep_per_guard[last_guard] += asleep_time
        for i in range(asleep_time):
            idx = start_time + i
            if idx not in asleep_per_guard_per_minute[last_guard]:
                asleep_per_guard_per_minute[last_guard][idx] = 0

            print(
                f"Setting idx {idx} to {asleep_per_guard_per_minute[last_guard][idx] + 1}"
            )
            asleep_per_guard_per_minute[last_guard][idx] += 1


# max_time_asleep = 0
# max_guard = None
# for guard_id, sleep_time in asleep_per_guard.items():
#    if sleep_time > max_time_asleep:
#        print("Guard overwrite")
#        max_guard = guard_id
#        max_time_asleep = sleep_time

# print(f"Guard {max_guard} sleeps for {max_time_asleep}")

pp.pprint(asleep_per_guard_per_minute)
max_occurence = 0
max_minute = None
max_guard = None
for guard in asleep_per_guard_per_minute.keys():
    for minute, occurence in asleep_per_guard_per_minute[guard].items():
        if occurence > max_occurence:
            max_occurence = occurence
            max_minute = minute
            max_guard = guard

print(
    "Max occurence: ",
    max_occurence,
    " Max minute: ",
    max_minute,
    " solution: ",
    max_minute * max_guard,
)
