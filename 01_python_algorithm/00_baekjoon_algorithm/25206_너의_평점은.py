
import sys

input = sys.stdin.readline

def main():

  sum = 0.0
  subject_list = []
  for _ in range(20):
    result = list(map(str, input().split()))
    if result[2] == 'A+':
      result[2] = 4.5
    elif result[2] == 'A0':
      result[2] = 4.0
    elif result[2] == 'B+':
      result[2] = 3.5
    elif result[2] == 'B0':
      result[2] = 3.0
    elif result[2] == 'C+':
      result[2] = 2.5
    elif result[2] == 'C0':
      result[2] = 2.0
    elif result[2] == 'D+':
      result[2] = 1.5
    elif result[2] == 'D0':
      result[2] = 1.0
    elif result[2] == 'F':
      result[2] = 0.0
    else:
      continue
    sum += float(result[1])
    subject_list.append(float(result[1]) * float(result[2]))

  sum_list = 0.0
  for i in subject_list:
    sum_list+=i
  print(round((sum_list/ sum), 6))

if __name__ == '__main__':
  main()