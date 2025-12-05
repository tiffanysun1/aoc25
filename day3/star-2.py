file_path = "day3/input.txt"
total = 0
with open(file_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        joltage = ""
        batteries = [int(l) for l in line.strip()]
        first_j = 0

        for i in range(11, -1, -1):
            first = float("inf") * -1
            for j in range(first_j, len(batteries) - i):
                battery = batteries[j]
                if battery > first:
                    first = battery
                    first_j = j + 1
            joltage += str(first)
        total += int(joltage)

    print(total)
