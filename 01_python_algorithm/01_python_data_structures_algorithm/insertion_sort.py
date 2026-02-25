
# 삽입 정렬은 인덱스 1부터 시작
# 데이터가 거의 정렬되어 있을 때는 O(N)이지만 아닐 경우에는 평균/최악 시간 복잡도가 O(N²)이므로 잘 사용하지 않는다.
def insertion_sort(a_list: list[int]) -> list[int]:
    for i in range(1, len(a_list)): # 1 ~ 4
        value = a_list[i]
        while i > 0 and a_list[i -1] > value:
            a_list[i] = a_list[i - 1]
            i = i - 1
        a_list[i] = value
    return a_list



if __name__ == '__main__':
    print(insertion_sort([3, 2, 9, 8, 10]))