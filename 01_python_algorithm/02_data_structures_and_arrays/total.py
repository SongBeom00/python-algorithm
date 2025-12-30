
print('학생 그룹 점수의 합계와 평균을 구합니다')

scores1 = int(input('1번 학생의 점수를 입력하세요'))
scores2 = int(input('2번 학생의 점수를 입력하세요'))
scores3 = int(input('3번 학생의 점수를 입력하세요'))
scores4 = int(input('4번 학생의 점수를 입력하세요'))
scores5 = int(input('5번 학생의 점수를 입력하세요'))

total = 0
total += scores1
total += scores2
total += scores3
total += scores4
total += scores5

print(f'합계는 {total}점 입니다.')
print(f'평균은 {total / 5}점 입니다.')