# 문자열 기본 기능

# 문자열 생성
a = "Hello, World!"

# 문자열 길이 확인
len(a)  # 결과: 13

# 문자열 인덱싱
a[1]  # 결과: 'e'

# 문자열 슬라이싱
a[2:5]  # 결과: 'llo'

# 문자열 수정
a.upper()  # 결과: 'HELLO, WORLD!'
a.lower()  # 결과: 'hello, world!'
a.strip()  # 결과: 'Hello, World!'
a.replace("H", "J")  # 결과: 'Jello, World!'
a.split(",")  # 결과: ['Hello', ' World!']

# 문자열 연결
b = " How are you?"
a + b  # 결과: 'Hello, World! How are you?'
"{} How are you?".format(a)  # 결과: 'Hello, World! How are you?'

# 이스케이프 문자
txt = "We are the so-called \"Vikings\" from the north."  # 결과: 'We are the so-called "Vikings" from the north.'

# 연산자

# 산술 연산자
x = 10
y = 5
x + y  # 결과: 15
x - y  # 결과: 5
x * y  # 결과: 50
x / y  # 결과: 2.0
x % y  # 결과: 0
x ** y  # 결과: 100
x // y  # 결과: 2

# 할당 연산자
x = 5
x += 3  # 결과: 8
x -= 3  # 결과: 2
x *= 3  # 결과: 15
x /= 3  # 결과: 5.0
x %= 3  # 결과: 2
x //= 3  # 결과: 0
x **= 3  # 결과: 0

# 비교 연산자
x = 5
y = 3
x == y  # 결과: False
x != y  # 결과: True
x > y  # 결과: True
x < y  # 결과: False
x >= y  # 결과: True
x <= y  # 결과: False

# 논리 연산자
x = 5
x > 3 and x < 10  # 결과: True
x > 3 or x < 4  # 결과: True
not(x > 3 and x < 10)  # 결과: False

# 리스트 기본 기능

# 리스트 생성
thislist = ['apple', 'banana', 'cherry']

# 리스트 인덱싱 및 슬라이싱
thislist[1]  # 결과: 'banana'
thislist[2:5]  # 결과: ['cherry']

# 리스트 항목 추가/제거
thislist.append('orange')  # 결과: ['apple', 'banana', 'cherry', 'orange']
thislist.insert(1, 'watermelon')  # 결과: ['apple', 'watermelon', 'banana', 'cherry', 'orange']
thislist.remove('banana')  # 결과: ['apple', 'watermelon', 'cherry', 'orange']
thislist.clear()  # 결과: []

# 리스트 확장
thislist = ['apple', 'banana', 'cherry']
tropical = ['mango', 'pineapple', 'papaya']
thislist.extend(tropical)  # 결과: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# 리스트 컴프리헨션
fruits_with_a = [x for x in thislist if "a" in x]  # 결과: ['banana', 'mango', 'pineapple', 'papaya']

# 리스트 정렬
thislist.sort()  # 결과: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
thislist.sort(reverse=True)  # 결과: ['papaya', 'pineapple', 'mango', 'cherry', 'banana', 'apple']

# 루프

# While 루프
i = 1
while i < 6:
    print(i)
    i += 1
# 결과:
# 1
# 2
# 3
# 4
# 5

# Break 문
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
# 결과:
# 1
# 2
# 3

# Continue 문
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
# 결과:
# 1
# 2
# 4
# 5
# 6

# For 루프
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
# 결과:
# apple
# banana
# cherry

# For Else 문
for x in range(6):
    print(x)
else:
    print("Finally finished!")
# 결과:
# 0
# 1
# 2
# 3
# 4
# 5
# Finally finished!

# 중첩 루프
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
# 결과:
# red apple
# red banana
# red cherry
# big apple
# big banana
# big cherry
# tasty apple
# tasty banana
# tasty cherry

# 추가 기능

# In 연산자
txt = "apple" in fruits  # 결과: True

# Remove 문
fruits.remove("banana")  # 결과: ['apple', 'cherry']

# Clear 문
fruits.clear()  # 결과: []

# While 루프 사용 예시
i = 0
while i < 10:
    print(i)
    i += 1
# 결과:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
