def factorial1(n : int) -> int:
  if n == 0 : return 1
  sum = 1
  for i in range(1, n+1):
    sum *= i
  return sum

def factorial2(n):
  if n == 0 :
    return 1
  return n * factorial2(n - 1)

# 1부터 10까지의 숫자를 재귀로 출력해보기
def factorial3(start: int, end: int):
  if start > end :
    return
  print(start)
  return factorial3(start+1, 10)


if __name__ == '__main__':
  factorial3(start=1, end=10)

