# 시퀀스 원소의 최대값 출력하기

from typing import Any, Sequence

# Any는 제약이 없는 임의의 자료형을 의미합니다.
# Sequence는 리스트, 바이트 배열, 문자열, 튜플, 바이트열이 있습니다.
def main():
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요:'))
    x = [None] * num # 원소 수가 num인 리스트를 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요'))

    print(f'최대값은 {max_of(x)} 값입니다.')

def max_of(a: Sequence) -> Any:
    """시퀀스 a 원소의 최댓값을 반환"""
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

if __name__  == '__main__':
    main()

