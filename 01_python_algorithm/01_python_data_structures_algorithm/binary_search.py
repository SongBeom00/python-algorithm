

def binary_search(search_list: list[int], target: int) -> bool:
  first = 0
  last = len(search_list) - 1
  while last >= first:
      mid = (first + last) // 2 # 몫 연산자
      if search_list[mid] == target:
        return True
      else:
        if target < search_list[mid]:
          last = mid - 1
        else:
          first = mid + 1
  return False


if __name__ == '__main__':
  print(binary_search([10, 12, 13, 14, 15, 18, 19], 1))