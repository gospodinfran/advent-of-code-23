file = open('input.txt', 'r')
lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()


def check_up(lines, i, j):
    if i - 1 < 0:
        return False
    c = lines[i-1][j]
    if (not c.isnumeric() and c != '.'):
        return True


def check_right(lines, i, j):
    if j + 1 > len(lines[0]) - 1:
        return False
    c = lines[i][j+1]
    if (not c.isnumeric() and c != '.'):
        return True


def check_left(lines, i, j):
    if j - 1 < 0:
        return False
    c = lines[i][j-1]
    if (not c.isnumeric() and c != '.'):
        return True


def check_down(lines, i, j):
    if i + 1 > len(lines) - 1:
        return False
    c = lines[i+1][j]
    if (not c.isnumeric() and c != '.'):
        return True


def check_top_left(lines, i, j):
    if i - 1 < 0 or j - 1 < 0:
        return False
    c = lines[i-1][j-1]
    if (not c.isnumeric() and c != '.'):
        return True


def check_top_right(lines, i, j):
    if i - 1 < 0 or j + 1 > len(lines[0]) - 1:
        return False
    c = lines[i-1][j+1]
    if (not c.isnumeric() and c != '.'):
        return True


def check_bottom_left(lines, i, j):
    if i + 1 > len(lines) - 1 or j - 1 < 0:
        return False
    c = lines[i+1][j-1]
    if (not c.isnumeric() and c != '.'):
        return True


def check_bottom_right(lines, i, j):
    if i + 1 > len(lines) - 1 or j + 1 > len(lines[0]) - 1:
        return False
    c = lines[i+1][j+1]
    if (not c.isnumeric() and c != '.'):
        return True


def check_all_positions(lines, i, j):
    return check_up(lines, i, j) or check_down(lines, i, j) or check_left(lines, i, j) or check_right(lines, i, j) or check_top_left(lines, i, j) or check_top_right(lines, i, j) or check_bottom_left(lines, i, j) or check_bottom_right(lines, i, j)


part_nums = []
skip = 0

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if skip > 0:
            skip -= 1
            if skip == 0:
                start, end = j, j
                while start-1 >= 0 and lines[i][start-1].isnumeric():
                    start -= 1
                while end+1 < len(lines[0]) and lines[i][end+1].isnumeric():
                    end += 1
                part_nums.append(int(lines[i][start:end+1]))
            continue
        if not lines[i][j].isnumeric():
            continue

        nr_digits = 0
        while j+nr_digits < len(lines[0]) and lines[i][j+nr_digits].isnumeric():
            nr_digits += 1

        # Top left corner
        part_num = check_all_positions(lines, i, j)

        if part_num:
            start, end = j, j
            while start-1 >= 0 and lines[i][start-1].isnumeric():
                start -= 1
            while end+1 < len(lines[0]) and lines[i][end+1].isnumeric():
                end += 1

            if end == j:
                part_nums.append(int(lines[i][start:end+1]))
            else:
                skip = end - j

print(sum(part_nums))
shortest, longest = part_nums[0], part_nums[0]
for n in part_nums:
    if len(str(n)) < len(str(shortest)):
        shortest = n
    if len(str(n)) > len(str(longest)):
        longest = n
print('shortest:', shortest)
print('longest:', longest)
