# 1부터 n까지 정수의 합 구하기

def sum_1ton(n: int) -> int:
    """1부터 n까지 정수의 합"""
    s = 0
    while n > 0:
        s += n
        n -= 1

    return s


def main():
    x = int(input('x의 값을 입력하세요: '))
    print(f'1부터 {x}까지의 합은 {sum_1ton(x)}입니다.')


if __name__ == '__main__':
    main()