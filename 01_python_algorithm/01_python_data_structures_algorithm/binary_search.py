from bisect import bisect_left
from typing import Protocol, TypeVar, Any


class Comparable(Protocol):
  def __lt__(self, other: 'Comparable') -> bool: ...

T = TypeVar('T', bound=Comparable)



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

def binary_search2(search_list: list[Any], target: Any) -> bool:
  index = bisect_left(search_list, target)
  return index < len(search_list) and search_list[index] == target

def binary_search3(search_list: List[T], target: T) -> bool:
  index = bisect_left(search_list, target)
  return index < len(search_list) and search_list[index] == target


if __name__ == '__main__':
  print(binary_search([10, 12, 13, 14, 15, 18, 19], 19))
  sorted_fruits = ['apple', 'banana', 'orange', 'plum']
  print(bisect_left(sorted_fruits, 'banana')) # 인덱스 위치 1 반환
  print(bisect_left(sorted_fruits, 'kiwi')) # 존재했다면 있었을 인덱스 2 반환

  print(binary_search2([10, 12, 13, 14, 15, 18, 19], 19))
  print(binary_search2(sorted_fruits, 'kiwi'))

  print(ord('A')) # 65
  print(ord('a')) # 97

