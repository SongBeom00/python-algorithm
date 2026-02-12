

def linear_search(a_list: list[int], n : int) -> bool:
  for i in a_list:
      if i == n:
        return True
  return False




if __name__  == '__main__':
  a_list = [1, 8, 32, 91, 5, 15, 9, 100, 3]
  print(linear_search(a_list, 100))
  unsorted_list = [1, 45, 4, 32, 3]
  print(45 in unsorted_list)
  print('a' in 'apple') # 문자열에서도 선형 탐색을 수행합니다.
