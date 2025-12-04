file_path = "day2/input.txt"
total = 0
with open(file_path, "r") as file:
    line = file.read()
    ids = line.split(",")
    for i in ids:
        first, last = i.split("-")
        for j in range(int(first), int(last) + 1):
            j_str = str(j)
            if j_str[0] != "0":
                half_1 = j_str[0 : len(j_str) // 2]
                half_2 = j_str[len(j_str) // 2 :]
                if half_1 == half_2:
                    total += j

    print(total)
