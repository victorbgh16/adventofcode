with open('input') as f:
    data = f.readlines()

processed = []

for elem in data:
    curr = [*elem]
    # print(curr)
    tmp = []
    for _ in curr:
        if _.isnumeric():
            tmp.append(_)
    processed.append(tmp)

numbers = []

for elem in processed:
    numbers.append(str(elem[0]) + str(elem[-1]))

print(numbers)

total = 0
for num in numbers:
    total += int(num)

print(total)

nums = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

import re

stuff = []

for line in data:
    curr = [*_]
    tmp = []
    has_num_first_digit = False
    has_num_last_digit = False
    if str(curr[0]).isnumeric():
        tmp.append(curr[0])
        has_num_first_digit = True

    if str(curr[-1]).isnumeric():
        # tmp.append(curr[-1])
        has_num_last_digit = True

    results = re.findall('(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))', line)

    a = None
    b = None

    for result in results:
        if result.isnumeric():
            if a is None:
                a = result
                b = result
            else:
                b = result
        else:
            if a is None:
                a = nums[result]
                b = nums[result]
            else:
                b = nums[result]
    stuff.append(int(f"{a}{b}"))
result = sum(stuff)
print(result)