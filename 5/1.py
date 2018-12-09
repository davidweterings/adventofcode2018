line = open("input.txt").read().strip()


def react(polymer):
    stack = []
    last_char = ""
    i = 0
    line = polymer
    max_length = len(line)
    while i < max_length:
        stack = []
        last_char = ""
        for char in line:
            if (last_char.lower() == char.lower()) and (
                (last_char.isupper() and char.islower())
                or (last_char.islower() and char.isupper())
            ):
                stack.pop()
                line = "".join(stack) + line[i + 1 :]
                # print("Reacting: ", last_char, char)
                # print("New line is: ", line)
                max_length = len(line)
                i = 0
                break
            else:
                stack.append(char)
                last_char = char
                i += 1
    return len(line)


print(react(line))
