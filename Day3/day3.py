file = open('input.txt', 'r')
lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

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

        part_num = False
        rows, cols = len(lines), len(lines[0])
        # Top left corner
        if i == 0 and j == 0:
            if (not lines[i+1][j].isnumeric() and lines[i+1][j] != '.') or (not lines[i+1][j+1].isnumeric() and lines[i+1][j+1] != '.'):
                part_num = True
        # Top right corner
        elif i == 0 and j == cols-1:
            if (not lines[i+1][j].isnumeric() and lines[i+1][j] != '.') or (not lines[i+1][j-1].isnumeric() and lines[i+1][j-1] != '.'):
                part_num = True
        # Top edge, not corner
        elif i == 0:
            if (not lines[i+1][j].isnumeric() and lines[i+1][j] != '.') or (not lines[i][j-1].isnumeric() and lines[i][j-1] != '.') or (not lines[i][j+1].isnumeric() and lines[i][j+1] != '.') or (not lines[i+1][j+1].isnumeric() and lines[i+1][j+1] != '.') or (not lines[i+1][j-1].isnumeric() and lines[i+1][j-1] != '.'):
                part_num = True
        # Bottom left corner
        elif i == rows-1 and j == 0:
            if (not lines[i-1][j].isnumeric() and lines[i-1][j] != '.') or (not lines[i-1][j+1].isnumeric() and lines[i-1][j+1] != '.'):
                part_num = True
        # Bottom right corner
        elif i == rows-1 and j == cols-1:
            if (not lines[i-1][j].isnumeric() and lines[i-1][j] != '.') or (not lines[i-1][j-1].isnumeric() and lines[i-1][j-1] != '.'):
                part_num = True
        # Bottom edge, not corner
        elif i == rows-1:
            if (not lines[i-1][j].isnumeric() and lines[i-1][j] != '.') or (not lines[i][j-1].isnumeric() and lines[i][j-1] != '.') or (not lines[i][j+1].isnumeric() and lines[i][j+1] != '.') or (not lines[i-1][j+1].isnumeric() and lines[i-1][j+1] != '.') or (not lines[i-1][j-1].isnumeric() and lines[i-1][j-1] != '.'):
                part_num = True
        # Left edge
        elif j == 0:
            if (not lines[i][j+1].isnumeric() and lines[i][j+1] != '.') or (not lines[i-1][j+1].isnumeric() and lines[i-1][j+1] != '.') or (not lines[i+1][j+1].isnumeric() and lines[i+1][j+1] != '.'):
                part_num = True
        # Right edge
        elif j == cols-1:
            if (not lines[i][j-1].isnumeric() and lines[i][j-1] != '.') or (not lines[i-1][j-1].isnumeric() and lines[i-1][j-1] != '.') or (not lines[i+1][j-1].isnumeric() and lines[i+1][j-1] != '.'):
                part_num = True
        else:
            if (not lines[i-1][j].isnumeric() and lines[i-1][j] != '.') or (not lines[i+1][j].isnumeric() and lines[i+1][j] != '.') or (not lines[i][j-1].isnumeric() and lines[i][j-1] != '.') or (not lines[i][j+1].isnumeric() and lines[i][j+1] != '.') or (not lines[i-1][j-1].isnumeric() and lines[i-1][j-1] != '.') or (not lines[i-1][j+1].isnumeric() and lines[i-1][j+1] != '.') or (not lines[i+1][j-1].isnumeric() and lines[i+1][j-1] != '.') or (not lines[i+1][j+1].isnumeric() and lines[i+1][j+1] != '.'):
                part_num = True

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
