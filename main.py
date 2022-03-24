def prettify(ugly_list):
    for row in ugly_list:
        print(row)


input = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

output = [[0 for j in range(len(input[0]))] for i in range(len(input))]

# 1 -> Black
# 0 -> White

check_dump = []

for row_i, row_v in enumerate(input):

    for column_i, column_v in enumerate(row_v):

        # Action on edges
        if (row_i == 0 or row_i == len(input) - 1 or column_i == 0 or column_i == len(input[0]) - 1) and column_v == 1:
            output[row_i][column_i] = 1
            check_cache = ([[row_i, column_i]] if not [row_i, column_i] in check_dump else [])

            while len(check_cache) != 0:
                x, y = check_cache.pop()
                check_dump.append([x, y])

                # North
                if x != 0 and (
                        input[x - 1][y] == 1 and ([x - 1, y] not in check_cache and [x - 1, y] not in check_dump)):
                    output[x - 1][y] = 1
                    check_cache.append([x - 1, y])

                # South
                if x != len(input) - 1 and (
                        input[x + 1][y] == 1 and ([x + 1, y] not in check_cache and [x + 1, y] not in check_dump)):
                    output[x + 1][y] = 1
                    check_cache.append([x + 1, y])

                # East
                if y != 0 and (
                        input[x][y - 1] == 1 and ([x, y - 1] not in check_cache and [x, y - 1] not in check_dump)):
                    output[x][y - 1] = 1
                    check_cache.append([x, y - 1])

                # West
                if y != len(input[0]) - 1 and (
                        input[x][y + 1] == 1 and ([x, y + 1] not in check_cache and [x, y + 1] not in check_dump)):
                    output[x][y + 1] = 1
                    check_cache.append([x, y + 1])

print("----------| INPUT |----------")
prettify(input)
print("----------| OUTPUT |----------")
prettify(output)
