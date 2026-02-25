
a_list = [1, 8, 10, 33, 4, 103]
print(sorted(a_list))

print(sorted(a_list, reverse=True)) # 옵션으로 reverse를 매개변수로 받습니다.


a_list = ['Guido van Rossum', 'James Gosling', 'Brendan Eich', 'Yukihiro Matsmoto']
print(sorted(a_list)) # 각 문자열의 첫 번째 글자를 알파벳 순으로 정렬한 새로운 리스트를 반환

a_list = ['onehundred', 'five', 'seventy', 'two']
print(sorted(a_list, key=len)) # 문자열 길이를 기준으로 정렬합니다.

# sort() 함수
# sort 함수는 sorted 처럼 새로운 리스트를 반환하지 않고, 원래 리스트를 수정합니다.
a_list = [1, 8, 10, 33, 4, 103]
a_list.sort() # None
print(a_list)
