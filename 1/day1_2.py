import sys

frequency = 0
seen_freqs = set()
while True:
    print("Looping input again")
    with open('input.txt') as fh:
        for line in fh:
            if line:
                frequency += int(line)
                if frequency not in seen_freqs:
                    seen_freqs.add(frequency)
                else:
                    print("First seen frequency twice: ", frequency)
                    sys.exit(0)

