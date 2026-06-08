# Python Basic 노트북 정리 (1~9)

---

## 1. Naming Convention — 변수 명명 규칙

- 영문자와 숫자 사용 가능, **대소문자 구분**
- **문자 또는 `_`로 시작** (숫자 시작 불가)
- 특수문자(`+`, `-`, `*`, `@`, `#` 등) 불가

```python
a = 15       # OK
_b = 3.14    # OK
_7d = 5.14   # OK
# 2c = 77   # 숫자 시작 불가
```

---

## 2. Assigning & Comparison — 할당 & 비교

| 연산자 | 의미 |
|--------|------|
| `==`, `!=` | **값(value)** 비교 |
| `is`, `is not` | **객체(참조, 주소)** 비교 |

- 정수 `-5~256` 범위는 파이썬이 캐싱 → 같은 객체
- 리스트는 `y = x`로 할당하면 **같은 객체 참조**, `y = ['a']`처럼 새로 만들면 **다른 객체**

```python
x = ['orange', 'banana']
y = x
x is y  # True (같은 주소)

y = ['orange', 'banana']
x is y  # False (다른 주소, 값은 같음)
```

---

## 3. TypeError Handling — 타입 에러 처리

- 문자열 <-> 정수 연산 시 **형변환(Type Casting)** 필요
- 문자열을 함수처럼 호출하면 `TypeError: 'str' object is not callable`
- 리스트 인덱스는 반드시 **정수**로 접근

```python
x = "Seoul"
y = str(25)      # 형변환
z = x + y        # "Seoul25"

c = [1, 2, 3]
# c["2"]         # 인덱스는 정수여야 함
c[1:3]           # OK -> [2, 3]
```

---

## 4. Sequence Type Indexing — 시퀀스 인덱싱

- 시퀀스 타입: `List`, `Tuple`, `str`, `range`
- 주요 메서드: `append`, `extend`, `index`, `insert`, `pop`, `remove`, `reverse`, `sort`

| 함수 | 설명 |
|------|------|
| `sort()` | 리스트 **자체**를 정렬, 반환값 `None` |
| `sorted()` | **새 리스트** 반환, 원본 유지 |

```python
x = ['Orange', 'Cherry', 'Apple', 'Kiwi', 'Banana']
x.index('Banana')              # 4
x.index('Banana', 1, len(x))  # 시작/끝 인덱스 지정 가능
```

---

## 5. Sequence Type Slicing — 시퀀스 슬라이싱

- `[start:end:step]` 형식, 음수 인덱스 사용 가능

```python
x = ['a','b','c','d','e','f','g','h','i','j','k','l','m']

# ['e', 'f', 'g'] 추출 — 다양한 방법
x[4:7]                     # 양수 인덱스
x[-9:-6]                   # 음수 인덱스
x[4:-6]                    # 혼합
x[-9:7]                    # 혼합
x[6:3:-1]                  # 역방향 -> ['g','f','e']
list(reversed(x[6:3:-1]))  # -> ['e','f','g']
```

---

## 6. Sequence Item Selection — 시퀀스 아이템 선택

리스트에서 조건에 맞는 항목을 추출하는 **4가지 방법** 비교:

```python
x = ['grapes', 'mango', 'apple', 'kiwi', ...]

# 1) index로 직접 접근
result1.append(x[x.index('apple')].upper())

# 2) for 루프
for i in x:
    if i == 'apple' or i == 'kiwi':
        result.append(i.upper())

# 3) map + filter + lambda
list(map(lambda b: b.upper(), filter(lambda a: a in ('apple', 'kiwi'), x)))

# 4) 리스트 컴프리헨션 (가장 간결)
[i.upper() for i in x if i == 'apple' or i == 'kiwi']

# 모두 결과: ['APPLE', 'KIWI']
```

---

## 7. Range Technique — range 활용

30부터 -10까지 -2씩 감소하는 리스트를 만드는 **5가지 방법**:

```python
# 1) range에 step 직접 지정
[i for i in range(30, -11, -2)]

# 2) 반대 방향으로 만든 뒤 reversed
list(reversed([i for i in range(-10, 31, 2)]))

# 3) 전체 range에서 짝수 필터링
[i for i in range(30, -11, -1) if i % 2 == 0]

# 4) 반대 방향 + 짝수 필터 + reversed
list(reversed([i for i in range(-11, 31) if i % 2 == 0]))

# 5) list(range(...)) 직접 변환
list(range(30, -11, -2))

# 결과: [30, 28, 26, ..., -8, -10]
```

---

## 8. More Range Technique — range 심화

1~20에서 **홀수는 x10, 짝수는 그대로** 출력하는 2가지 방법:

```python
# 1) for 루프 + if/else
for i in range(1, 21):
    if i % 2 != 0:
        result.append(i * 10)
    else:
        result.append(i)

# 2) 조건부 표현식(삼항연산자) + 리스트 컴프리헨션
result = [i * 10 if i % 2 != 0 else i for i in range(1, 21)]

# 결과: [10, 2, 30, 4, 50, 6, ..., 190, 20]
```

---

## 9. Range & Map & Lambda — 종합 활용

1~15까지 각 원소에 x10 후 **문자열 리스트**로 출력하는 3가지 방법:

```python
# 1) for 루프
result = []
for i in range(1, 16):
    result.append(str(i * 10))

# 2) map + lambda (가장 함수형)
result = list(map(lambda x: str(x * 10), range(1, 16)))

# 3) 리스트 컴프리헨션
result = [str(i * 10) for i in range(1, 16)]

# 결과: ['10', '20', '30', ..., '140', '150']
```

| 방법 | 특징 |
|------|------|
| `for` 루프 | 가장 직관적 |
| `map + lambda` | 함수형 스타일, 지연 평가(lazy) |
| 리스트 컴프리헨션 | 간결하고 Pythonic |

---

## 10. Remove Duplicates — 중복 제거

- `set` : 중복 허용 X, **순서 X**
- `list` : 중복 허용 O, 순서 O
- Python 3.7 이상에서는 `dict`도 삽입 순서 보장

```python
x = ['a', 1, 'b', 2, 'a', 3, 'b', 4, 5, 'b']

# 1) set 변환 — 순서 보장 안됨
list(set(x))  # [1, 'b', 3, 2, 4, 5, 'a'] (순서 무작위)

# 2) OrderedDict — 순서 유지
from collections import OrderedDict
list(OrderedDict.fromkeys(x))  # ['a', 1, 'b', 2, 3, 4, 5]

# 3) for 루프 — 순서 유지
result = []
for i in x:
    if i not in result:
        result.append(i)

# 4) dict.fromkeys — 순서 유지 (Python 3.7+, 가장 간결)
list(dict.fromkeys(x))  # ['a', 1, 'b', 2, 3, 4, 5]
```

| 방법 | 순서 유지 | 특징 |
|------|-----------|------|
| `set` | X | 가장 빠름 |
| `OrderedDict.fromkeys` | O | 구버전 호환 |
| `for` 루프 | O | 직관적 |
| `dict.fromkeys` | O | Python 3.7+, 권장 |

---

## 전체 흐름 요약

```
변수 규칙 -> 비교 연산 -> 타입 에러 -> 인덱싱 -> 슬라이싱 -> 아이템 선택 -> range 기초 -> range 심화 -> map/lambda 종합 -> 중복 제거
```

기초 문법에서 시작해 시퀀스 자료형 조작, 리스트 컴프리헨션, 람다/map, 집합 자료형 등 점진적으로 심화되는 구성입니다.
