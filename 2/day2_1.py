from collections import Counter


amount_twos = 0
amount_threes = 0
with open("input.txt") as fh:
    for line in fh:
        if line:
            counter = Counter(line)
            if any(amount == 2 for amount in counter.values()):
                amount_twos += 1
            if any(amount == 3 for amount in counter.values()):
                amount_threes += 1

print("Amount twos", amount_twos)
print("Amount threes", amount_threes)
print("Checksum", amount_twos * amount_threes)
