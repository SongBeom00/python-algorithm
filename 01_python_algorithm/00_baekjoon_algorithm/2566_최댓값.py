

def main1():
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

import sys

input = sys.stdin.readline

def main2():
  max_value = -1
  result = [0 , 0]
  for i in range(3):
    row = list(map(int, input().split()))
    max_row = max(row)
    for j in range(3):
      if max_value < max_row:
        max_value = max_row
        result[0] = i + 1
        result[1] = row.index(max_value) + 1
  print(max_value)
  print(*result)


if __name__ == '__main__':
  # main1()
  main2()



