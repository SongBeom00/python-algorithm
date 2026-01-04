# 리스트에서 임의의 원솟값을 업데이트하기
from typing import List


def change(lst: List, idx: int, val: int) -> None:
    """lst[idx]의 값을 val로 업데이트"""
    lst[idx] = val


def main():
    x = [11, 22, 33, 44, 55]
    print('x = ', x)

    index = int(input('업데이트할 인덱스를 선택하세요: '))
    value = int(input('새로운 값을 입력하세요: '))

    change(lst=x, idx=index, val=value)
    print('x = ', x)

if __name__ == '__main__':
    main()