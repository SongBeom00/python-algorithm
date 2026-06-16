# Python Basic 노트북 정리 (1~18)

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

## 11. Dict Items Sum — 딕셔너리 활용

### 값 합산

```python
d = {'a': 17, 'b': 114, 'c': 247, 'd': 362, 'e': 220, 'f': 728, 'g': -283, 'h': 922}

# 1) for 루프
total = 0
for i in d.values():
    total += i

# 2) sum() (가장 간결)
sum(d.values())

# 3) 리스트 컴프리헨션
sum([d[item] for item in d])
```

### 항목 추가

```python
d = {'a': 'apple', 'b': 'grape'}

# update()로 여러 항목 추가
d.update({'c': 'banana', 'd': 'kiwi'})

# 직접 키 접근으로 추가
d['c'] = 'banana'
```

### 값 필터링 (value > 25)

```python
d = {'a': 8, 'b': 33, 'c': 15, 'd': 26, 'e': 12, 'f': 120}

# 1) filter + lambda — x[0]은 key, x[1]은 value
dict(filter(lambda x: x[1] > 25, d.items()))

# 2) 딕셔너리 컴프리헨션 (가장 Pythonic)
{k: v for k, v in d.items() if v > 25}

# 3) for 루프
result = {}
for k, v in d.items():
    if v > 25:
        result[k] = v
```

### 딕셔너리 순회

```python
d = dict(one=list(range(1, 11)), two=list(range(11, 23)), three=list(range(23, 37)))

for k, v in d.items():
    print(f'key "{k}" has values {v} -> total {len(v)}')

# get()으로 접근
def print_dict_summary(d: dict):
    for i in d.keys():
        values = d.get(i)
        print(f"key '{i}' has values {values} -> total : {len(values)}")
```

---

## 12. Data Pretty Printer — pprint

- `pprint` : 중첩 구조를 **들여쓰기로 보기 좋게** 출력하는 표준 라이브러리
- API 응답 등 복잡한 JSON 확인 시 유용

```python
from urllib import request
import json
from pprint import pprint

response = request.urlopen('https://jsonplaceholder.typicode.com/users')
d = json.loads(response.read())

print(d)    # 한 줄로 출력 (가독성 낮음)
pprint(d)   # 들여쓰기 적용 (가독성 높음)
```

---

## 13. Sigma Calculator — 시그마 계산기

1부터 n까지의 합(Σ)을 구하는 **3가지 방법**:

```python
# 1) 수학 공식 (O(1), 가장 빠름)
def sigma_n1(n: int) -> int:
    return (n * (n + 1)) // 2

# 2) for 루프
def sigma_n2(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# 3) sum + range (가장 Pythonic)
def sigma_n3(n: int) -> int:
    return sum(range(1, n + 1))

sigma_n1(10)  # 55
```

| 방법 | 시간복잡도 | 특징 |
|------|-----------|------|
| 수학 공식 | O(1) | 가장 빠름 |
| `for` 루프 | O(n) | 직관적 |
| `sum(range(...))` | O(n) | 간결하고 Pythonic |

---

## 14. Function Arguments — 함수 인자

- 기본값 있는 매개변수는 반드시 **기본값 없는 매개변수 뒤**에 위치
- `*args` → 위치 인자를 **튜플(tuple)**로 받음
- `**kwargs` → 키워드 인자를 **딕셔너리(dict)**로 받음

```python
# 기본값 인자 (default argument)
def greet(name: str, msg: str = 'Good morning') -> str:
    return "Hi! " + name + ', ' + msg

greet("Kim")                    # "Hi! Kim, Good morning"
greet("Park", "How do you do?") # "Hi! Park, How do you do?"

# *args — 가변 위치 인자
def add(*args):
    return sum(args)

add(10, 20, 30)                     # 60
add(*(i for i in range(1, 101)))    # 5050 (언패킹으로 전달)

# **kwargs — 가변 키워드 인자
def info(**kwargs):
    print(kwargs)

info(name='Kim', age=30)   # {'name': 'Kim', 'age': 30}
info(**{'Kim': 30})        # {'Kim': 30}
```

---

## 15. Global Variables — 전역 변수

- 함수 내부에서 **전역 변수를 읽기만** 할 때는 그냥 접근 가능
- 함수 내부에서 **전역 변수에 값을 할당**하면 파이썬이 지역 변수로 판단 → `UnboundLocalError`
- 전역 변수를 수정하려면 `global` 키워드 선언 필요

```python
x = 100

# 읽기만 할 경우 — 정상 동작
def test():
    return x * 10

print(test())  # 1000

# 할당 시도 — UnboundLocalError 발생
def test_error():
    x = x * 10  # 지역 변수로 판단, 초기화 전 참조 에러
    return x

# global 키워드로 해결
def test_global():
    global x
    x = x * 10
    return x
```

---

## 16. Local Variables — 지역 변수

- 함수 내부에서 선언한 변수는 **지역 변수(local variable)** → 함수 밖에서 접근 불가
- 같은 이름의 전역 변수가 있어도, 함수 내에서 새로 할당하면 **별개의 지역 변수**로 동작
- `global` 선언 시 함수 내부에서 **전역 변수를 직접 수정** 가능

```python
a = 20

def test():
    a = 35      # 지역 변수 (전역 a와 별개)
    return a

print(a)        # 20 (전역)
print(test())   # 35 (지역)
print(a)        # 20 (전역 그대로)
```

```python
a = 20

def test():
    global a
    a = 35      # 전역 변수 수정
    return a

print(a)        # 20
a = 100
print(a)        # 100
print(test())   # 35
print(a)        # 35 (전역이 바뀜)
```

| 변수 유형 | 범위 | 특징 |
|-----------|------|------|
| 지역 변수 | 함수 내부 | 함수 종료 시 소멸 |
| 전역 변수 | 모듈 전체 | `global` 없이는 함수 내에서 수정 불가 |

---

## 17. String Split By Delimiter — 구분자로 문자열 분리

- `str.split()` : 공백 기준으로 분리, 리스트 반환
- `str.split(sep, maxsplit)` : 구분자와 분리 횟수 지정
- 파일에서 텍스트를 읽어 단어 수를 세는 실용 예제

```python
in_str = 'Suppose we have few words that are separated by spaces.'

a = in_str.split()       # 공백 기준 분리
print(len(a))            # 10

b = in_str.split('&', 2) # '&' 기준, 최대 2번만 분리
# ['orange', 'banana', 'apple&kiwi&watermelon']
```

```python
import re

def cnt_word(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        txt = file.read()

    # 방법 1: replace로 쉼표 제거 후 split
    txt_list = txt.replace(',', ' ').split()

    # 방법 2: 정규표현식으로 공백 또는 쉼표 기준 분리
    txt_list = re.split(' |,', txt)

    return len(txt_list)
```

| 방법 | 특징 |
|------|------|
| `split()` | 공백(스페이스·탭·개행) 기준, maxsplit 지정 가능 |
| `replace + split` | 특정 문자를 공백으로 치환 후 분리 |
| `re.split` | 복수 구분자를 정규식으로 처리 |

---

## 18. Alphabet in a File — 파일에 알파벳 쓰기

- `string.ascii_uppercase` : A~Z 대문자 알파벳 문자열
- `' '.join(iterable)` : 반복 가능 객체를 구분자로 연결
- 파일 쓰기(`'w'` 모드)와 `with open` 블록 활용

```python
import string

def file_write(file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        # 방법 1: for 루프
        for letter in string.ascii_uppercase:
            file.write(letter + ' ')

        # 방법 2: join (더 간결)
        file.write(' '.join(string.ascii_uppercase))
        # 결과: "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"

file_write('./source/23-1.txt')
```

| 요소 | 설명 |
|------|------|
| `string.ascii_uppercase` | `'ABCDEFGHIJKLMNOPQRSTUVWXYZ'` |
| `' '.join(...)` | 이터러블을 공백으로 연결 |
| `open(..., 'w')` | 파일 새로 쓰기 (없으면 생성, 있으면 덮어쓰기) |

---

## 전체 흐름 요약

```
변수 규칙 → 비교 연산 → 타입 에러 → 인덱싱 → 슬라이싱 → 아이템 선택
→ range 기초 → range 심화 → map/lambda 종합 → 중복 제거
→ 딕셔너리 활용 → pprint → 시그마 계산기 → 함수 인자 → 전역 변수
→ 지역 변수 → 문자열 분리 → 파일 쓰기
```

기초 문법에서 시작해 시퀀스 자료형 조작, 리스트 컴프리헨션, 람다/map, 딕셔너리, 함수 심화(가변 인자, 전역·지역 변수), 문자열 처리, 파일 I/O까지 점진적으로 심화되는 구성입니다.