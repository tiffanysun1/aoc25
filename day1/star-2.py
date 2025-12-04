pointer = 50
hits = 0

file_path = "day1/input.txt"

with open(file_path, "r") as file:
    for raw_line in file:
        line = raw_line.strip()
        if not line:
            continue

        direction = line[0]
        distance = int(line[1:])

        d = distance
        if direction == "R":
            if pointer == 0:
                first_zero_click = 100
            else:
                first_zero_click = 100 - pointer
        else:  # "L"
            if pointer == 0:
                first_zero_click = 100
            else:
                first_zero_click = pointer

        if d >= first_zero_click:
            hits += 1 + (d - first_zero_click) // 100

        step = 1 if direction == "R" else -1
        pointer = (pointer + step * d) % 100

print(hits)
