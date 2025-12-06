file_path = "day5/input.txt"
fresh = []
num_fresh = 0
fruits = []
# cases where overlap happens

# to_insert_vals = left, right
# existing = a, b

# if right is less than
# then range becomes left, max(b, right)
# pop a, b continue checking against others

# if left is less than b
# then range becomes min(a, left), right
# pop a, b continue checking
with open(file_path, "r") as file:
    lines = file.readlines()
    read_ranges = True
    for line in lines:
        if line.strip() == "":
            read_ranges = False
            print("done reading")
            # print(fresh)
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

for f in fruits:
    for left, right in fresh:
        if f >= left and f <= right:
            num_fresh += 1
            break

print(num_fresh)
# with open(file_path, "r") as file:
#     lines = file.readlines()
#     read_ranges = True
#     for line in lines:
#         if line.strip() == "":
#             read_ranges = False
#             print("done reading")
#             print(fresh)
#         elif read_ranges:
#             new_fresh = []
#             left, right = line.split("-")
#             left = int(left)
#             right = int(right)
#             for a, b in fresh:
#                 remove_a_b = False
#                 # print(a, b, left, right)
#                 if left <= b and left >= a:
#                     left = a
#                     right = max(b, right)
#                     remove_a_b = True
#                 if right >= a and right <= b:
#                     left = min(a, left)
#                     right = b
#                     remove_a_b = True
#                 if left <= a and right >= b:
#                     left = min(a, left)
#                     right = max(b, right)
#                     remove_a_b = True
#                 if not remove_a_b:
#                     new_fresh.append((a, b))
#                 right = max(b, right)
#             new_fresh.append((left, right))
#             # print(fresh)
#             fresh = new_fresh
#             # print(fresh)
#         else:
#             fruit = int(line.strip())
#             for left, right in fresh:
#                 if fruit >= left and fruit <= right:
#                     num_fresh += 1
# # print(fresh)
# print(num_fresh)
