file_path = "day3/input.txt"
total = 0
with open(file_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        batteries = [int(l) for l in line.strip()]
        print(batteries)
        first = float("inf") * -1
        second = float("inf") * -1
        first_i = 0
        for i in range(len(batteries)):
            battery = batteries[i]
            if battery > first:
                first = battery
                first_i = i
        if first_i == len(batteries) - 1:
            second = first
            first = max(batteries[:first_i])
        else:
            second = max(batteries[(first_i + 1) :])
        joltage = first * 10 + second
        print(joltage)
        total += joltage

    print(total)
