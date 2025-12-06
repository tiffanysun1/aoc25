file_path = "day5/input.txt"
num_fresh = 0
fresh = []
fruits = []

with open(file_path, "r") as file:
    lines = file.readlines()
    read_ranges = True
    for line in lines:
        if line.strip() == "":
            read_ranges = False
        elif read_ranges:
            left, right = line.split("-")
            fresh.append((int(left.strip()), int(right.strip())))
        else:
            fruits.append(int(line.strip()))


fresh.sort()
print(fruits, fresh)
new_fresh = []
left, right = fresh[0]
for a, b in fresh:
    if right < a:
        new_fresh.append((left, right))
        left, right = a, b
    else:
        right = max(right, b)
new_fresh.append((left, right))
print(new_fresh)

for left, right in new_fresh:
    num_fresh += right - left + 1
print(num_fresh)
