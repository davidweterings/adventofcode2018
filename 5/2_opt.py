import string
import sys

line = open("input.txt").read().strip()


def react(polymer):
    stack = [polymer[0]]
    last_char = polymer[0]
    for char in polymer[1:]:
        if (
            stack
            and (stack[-1].lower() == char.lower())
            and (
                (stack[-1].isupper() and char.islower())
                or (stack[-1].islower() and char.isupper())
            )
        ):
            stack.pop()
        else:
            stack.append(char)
    return len(stack)


min_react = sys.maxsize
best_char = None
for char in string.ascii_lowercase:
    new_len = react(line.replace(char, "").replace(char.upper(), ""))
    if new_len < min_react:
        min_react = new_len
        best_char = char

print(min_react, best_char)
