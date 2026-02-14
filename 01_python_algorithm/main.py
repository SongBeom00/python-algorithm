

max = -1
row = 0
col = 0

for i in range(9):
    col_list = list(map(int, input().split()))
    for j in range(9):
        if max <= col_list[j]:
            max = col_list[j]
            row = i + 1
            col = j + 1

print(max)
print(row, col)







