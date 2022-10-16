def read_data():
    with open("inputs/day-01.txt", "r") as file:
        return file.read()


def part_01():
    level = 0

    for element in read_data():
        if element == '(':
            level += 1
        elif element == ')':
            level -= 1

    return level


print(part_01())
