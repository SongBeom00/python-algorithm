
def bubble_sort1(array_list: list[int]):
  list_length = len(array_list) - 1
  for i in range(list_length):
    for j in range(list_length):
        if array_list[j] > array_list[j + 1]:
          array_list[j], array_list[j + 1] = array_list[j + 1], array_list[j]

  return array_list

def bubble_sort2(array_list: list[int]):
  list_length = len(array_list) - 1
  for i in range(list_length):
    for j in range(list_length - i):
        if array_list[j] > array_list[j + 1]:
          array_list[j], array_list[j + 1] = array_list[j + 1], array_list[j]

  return array_list

# swap이 안 일어날 경우 조기 종료
def bubble_sort3(array_list: list[int]):
  list_length = len(array_list) - 1
  for i in range(list_length):
    no_swaps = True
    for j in range(list_length):
      if array_list[j] > array_list[j+1]:
        array_list[j], array_list[j+1] = array_list[j+1], array_list[j]
        no_swaps = False
    if no_swaps: # 이미 정렬 완료
      return array_list
  return array_list

if __name__ == '__main__':
  array_list =  [32, 1, 9, 6]
  sort_list = bubble_sort3(array_list)
  print(sort_list)