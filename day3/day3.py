with open('example') as f:
    lines = [line + '.' for line in f.read().splitlines()]

print(lines)


def num_if_adjacent(line):
    adjacent = False

    number = ''
    first_index = 0

    for char in lines[line]:

        if char.isnumeric() and number == '':
            first_index = lines[line].index(char)

        if char.isnumeric():
            number += char

        if number != '' and not char.isnumeric():
            break

    if lines[line][first_index] is not None and not lines[line][first_index - 1].isalnum() and lines[line][first_index - 1] != '.':
        adjacent = True

    if lines[line][first_index] is not None and not lines[line][first_index + len(number)].isalnum() and lines[line][first_index + len(number)] != '.':
        adjacent = True

    if lines[line - 1] is not None and not lines[line - 1][first_index - 1].isalnum() and [lines][line - 1][first_index - 1] != '.':
        adjacent = True

    if lines[line - 1] is not None and not lines[line - 1][first_index + len(number)].isalnum() and [lines][line - 1][first_index + len(number)] != '.':
        adjacent = True

    if line + 1 < len(lines) and not lines[line + 1][first_index - 1].isalnum() and [lines][line + 1][first_index - 1] != '.':
        adjacent = True

    if line + 1 < len(lines) and not lines[line + 1][first_index + len(number)].isalnum() and [lines][line + 1][first_index + len(number)] != '.':
        adjacent = True

    if adjacent:
        return int(number)
    else:
        return 0


total = 0
for line in range(len(lines)):
    total += num_if_adjacent(line)

print(total)
