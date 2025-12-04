file_path = "day2/input.txt"
# total = 0
invalid_ids = []
with open(file_path, "r") as file:
    line = file.read()
    ids = line.split(",")
    for i in ids:
        first, last = i.split("-")
        for j in range(int(first), int(last) + 1):
            j_str = str(j)
            if j_str[0] != "0":
                length = len(j_str)
                for k in range(1, length):
                    if length % k == 0 and j_str.count(j_str[:k]) == (length // k):
                        print(j)
                        if j not in invalid_ids:
                            invalid_ids.append(j)

    print(sum(invalid_ids))
    # print(total)
