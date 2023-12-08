input = open('input.txt', 'r')

lines = input.readlines()


digits_spelled = {
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


def forward_search(line):
    for i, c in enumerate(line):
        if c.isnumeric():
            return str(c)

        else:
            for digit in digits_spelled:
                if digit in line[:i+1]:
                    return str(digits_spelled[digit])


def backward_search(line):
    for i in range(len(line)-1, -1, -1):
        if line[i].isnumeric():
            return str(line[i])
        else:
            for digit in digits_spelled:
                if digit in line[i:]:
                    return str(digits_spelled[digit])


res = 0
for line in lines:
    line = line.strip()

    tally = forward_search(line) + backward_search(line)
    res += int(tally)

print(res)
