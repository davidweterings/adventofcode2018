frequency = 0
with open('input.txt') as fh:
    for line in fh:
        if line:
            frequency += int(line)

print("Frequency is: ", frequency)
