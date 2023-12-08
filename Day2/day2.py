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
for game_id, line in enumerate(lines):
    over = False
    line = line.strip()

    counts = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    i = 0
    while line[i] != ':':
        i += 1

    while not over and i < len(line) - 1:
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
            # reset
            counts = {
                'red': 0,
                'green': 0,
                'blue': 0
            }

    if not over:
        res += game_id + 1

print('The answer is:', res)
