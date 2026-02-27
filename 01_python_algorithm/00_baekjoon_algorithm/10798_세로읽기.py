import sys

input = sys.stdin.readline


def main():

    result = []
    lines = [list(input().strip()) for _ in range(5)]

    max_len = max(len(line) for line in lines)

    for line in lines:
        while len(line) < max_len:
            line.append(' ')   # 공백 추가

    # print(lines)
    for i in range(max_len):
        for j in range(5):
            if lines[j][i] != ' ':
                result.append(lines[j][i])



        # for j in range(length):
        #     if lines[j][i] != '':
        #         result.append(lines[j][i])
    
    print(''.join(result))
    # result2 = ''.join(result)
    # print(result2 == 'Aa0aPAf985Bz1EhCz2W3D1gkD6x')


if __name__ == '__main__':
    main()