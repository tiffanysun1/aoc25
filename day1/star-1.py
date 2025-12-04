pointer = 50
hit = 0
file_path = "day1/input.txt"
with open(file_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        add = 1
        if line[0] == "L":
            add *= -1
        pointer = (pointer + add * int(line[1:])) % 100
        if pointer == 0:
            hit += 1
        # print(pointer)

print(hit)
