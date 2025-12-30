# 배열 원소의 최댓값을 구해서 출력하기(원솟값을 난수로 생성)

import random
from max import max_of

def main():
    print('난수의 최댓값을 구합니다.')
    num = int(input('난수의 개수를 입력하세요.: '))
    lo = int(input('난수의 최솟값을 입력하세요.: '))
    hi = int(input('난수의 최댓값을 입력하세요.: '))
    x = [None] * num # 원소 수가 num 인 리스트를 생성
    print(x)
    
    for i in range(num):
        x[i] = random.randint(lo, hi)

    print(f'[{x}]')
    print(f'이 가운데 최댓값을 {max_of(x)} 입니다.')

if __name__ == '__main__':
    main()