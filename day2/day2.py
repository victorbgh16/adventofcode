with open('input') as f:
    games = f.readlines()

total = 0

for e in games:
    id = e.split(':')[0]
    id = id.split()[1]
    values = e.split(':')[1].strip()
    values = values.split(';')
    # no_reds = 0
    # no_greens = 0
    # no_blues = 0

    limit_red = 12
    limit_green = 13
    limit_blue = 14

    invalid = False

    for elem in values:
        no_cubes = elem.split(',')

        for item in no_cubes:
            item = item.strip()

            num = int(item.split()[0])
            color = item.split()[1]

            if color == 'red' and num > limit_red:
                invalid = True
            elif color == 'green' and num > limit_green:
                invalid = True
            elif color == 'blue' and num > limit_blue:
                invalid = True

    if not invalid:
        total += int(id)

    # if no_reds <= 12 and no_greens <= 13 and no_blues <= 14:
    #     total += int(id)

print(total)