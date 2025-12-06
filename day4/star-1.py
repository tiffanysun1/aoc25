file_path = "day4/input.txt"
grid = []
with open(file_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        grid.append([l for l in line.strip()])

rows = len(grid)
cols = len(grid[0])
print(rows, cols, grid)
removed = 0
while True:
    can_be_removed = 0
    for i in range(rows):
        for j in range(cols):
            num_rolls = 0
            top = max(i - 1, 0)
            bot = min(i + 2, rows)
            left = max(j - 1, 0)
            right = min(j + 2, cols)
            # print("ranges", top, bot, left, right)
            if grid[i][j] == "@":
                # print(i, j)
                for k in range(left, right):
                    for l in range(top, bot):
                        # print(l, k, i, j)
                        if not (k == j and i == l):
                            if grid[l][k] == "@":
                                num_rolls += 1
                if num_rolls < 4:
                    # print(i, j, num_rolls)
                    grid[i][j] = "x"
                    removed += 1
                    can_be_removed += 1
    if can_be_removed == 0:
        break
print(removed)
# print(grid)
