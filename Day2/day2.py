input = open('input.txt', 'r')
lines = input.readlines()


def find_count_and_color(i, line):
    count = ''
    while line[i].isnumeric():
        count += line[i]
        i += 1

    i += 1
    color = ''
    while i < len(line) and line[i].isalpha():
        color += line[i]
        i += 1

    return [int(count), str(color), int(i)]


res = 0
sum_of_power = 0
finding_sum_ignore_over = True
for game_id, line in enumerate(lines):
    over = False
    line = line.strip()
    max_green = 0
    max_red = 0
    max_blue = 0

    counts = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    i = 0
    while line[i] != ':':
        i += 1

    while (not over or finding_sum_ignore_over) and i < len(line) - 1:
        # extraction
        while not line[i].isnumeric():
            i += 1
        count, color, index = find_count_and_color(i, line)
        if color in counts:
            counts[color] += count
        i = index

        # end of extraction, comma at position i if still going
        if i > len(line) - 1:
            i -= 1
        if line[i] != ',':
            # game over, check counts
            if counts['red'] > 12 or counts['green'] > 13 or counts['blue'] > 14:
                over = True
            # second star problem
            max_red = max(counts['red'], max_red)
            max_blue = max(counts['blue'], max_blue)
            max_green = max(counts['green'], max_green)
            # reset
            counts = {
                'red': 0,
                'green': 0,
                'blue': 0
            }

    if not over:
        res += game_id + 1
    sum_of_power += (max_red * max_blue * max_green)

print('The answer is:', res)
print('The sum of power of all the games is:', sum_of_power)
