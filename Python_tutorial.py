# Python-Tutorial

## Python Home
print("Hello, World!")  # 출력 함수를 이용하여 "Hello, World!"를 출력합니다.

## Python Syntax 
# Python Indentation
if 5 > 2:  # 만약 5가 2보다 크다면
    print("Five is greater than two!")  # "Five is greater than two!"를 출력합니다.

# Python Variables
x = 112  # 변수 x에 112를 할당합니다.
y = "Hello, World!"  # 변수 y에 "Hello, World!" 문자열을 할당합니다.

# Comment
# 코드의 한 줄을 주석 처리합니다.
# print("Hello, World!") 

# Python Comments
# 한 줄 주석
print("Hello, World!")  # 한 줄 끝에 주석을 작성합니다.

# Multiline Comments
"""
안녕하세요
감사합니다
잘 부탁드립니다
"""
print("Hello, World!")  # 여러 줄에 걸친 주석을 작성합니다.

## Python Variables
# 변수에 값을 할당합니다.
x = 10
y = "HoYoung"
print(x)
print(y)

# 다른 유형으로 변수를 설정합니다 (int : 정수형 , str : 문자열)
x = 5       # 정수형으로 작성된 변수
x = "Sally" # 문자열로 작성된 변수
print(x)

# 문자열, 정수형, 실수형 등 원하는 데이터 유형으로 지정할 수 있습니다.
x = str(3)    # x는 '3'이 됩니다.
y = int(3)    # y는 3이 됩니다.
z = float(3)  # z는 3.0이 됩니다.
print(type(x))
print(type(y))
print(type(z))

# 변수 이름은 대소문자를 구분하기 때문에 a, A 처럼 두 개의 변수를 설정할 수 있습니다.
### Variable Names
# 변수 이름은 문자나 밑줄 문자로 시작해야 합니다.
# 변수 이름은 숫자로 시작할 수 없습니다.
# 변수 이름에는 영숫자와 밑줄(Az, 0-9 및 _)만 포함할 수 있습니다.
# 변수 이름은 대소문자를 구분합니다(age, Age 및 AGE는 세 가지 다른 변수입니다).
myvar = "HoYoung"
my_var = "HoYoung"
_my_var = "HoYoung"
myVar = "HoYoung"
MYVAR = "HoYoung"
myvar2 = "HoYoung"

# 여러 변수에 대한 많은 값
# 한 줄로 여러 변수에 값을 할당합니다.
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# 컬렉션 압축 풀기
### 목록 압축 풀기 : 
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

## Output Variables
# 변수들을 출력합니다.
# 숫자의 경우 + 문자는 수학 연산자로 작동합니다.
x = 2
y = 3
print(x + y)

# 함수에서 print() 문자열과 숫자를 + 연산자와 결합하려고 하면 Python에서 오류를 표시합니다.
x = 5
y = "John"
print(str(x) + y)

# 함수에서 여러 변수를 출력하는 가장 좋은 방법은 print() 변수를 쉼표로 구분하는 것입니다.
x = 7
y = "HoYoung"
print(x, y)

## Python Data Types
# 데이터 유형을 가져옵니다.
x = 5
print(type(x))

## Python Numbers
# 숫자 유형에는 정수(int), 실수(float), 복소수(complex)가 있습니다.
# 한 유형에서 다른 유형으로 변환할 수 있습니다.
x = 1    # int
y = 2.8  # float
z = 1j   # complex

a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

## Python Strings
# 문자열 유형은 작은따옴표나 큰따옴표로 묶입니다.
# 변수에 문자열을 할당합니다.
a = "고마워"
print(a)

# 문자열 요소에 액세스합니다.
a = "안녕, 반가워"
print(a[1])

# 문자열을 반복하여 출력합니다.
for x in "catia":
    print(x)

# 문자열 길이를 출력합니다.
a = "Hello, World!"
print(len(a))

# 문자열 검사
txt = "안녕하세요, 반갑습니다"
print("고마워요" not in txt)

txt = "안녕하세요, 반갑습니다"
if "고마워요" not in txt:
    print("No, '고마워요' is NOT present.")
