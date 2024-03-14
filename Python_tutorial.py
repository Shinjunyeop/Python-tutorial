# Python-Tutorial

## Python Home
print("Hello, World!")  # 출력 함수를 이용하여 "Hello, World!"를 출력한다.

## Python Syntax 
# Python Indentation
if 5 > 2:  # 만약 5가 2보다 크다면
    print("Five is greater than two!")  # "Five is greater than two!"를 출력한다.

# Python Variables
x = 112  # 변수 x에 112를 할당한다.
y = "Hello, World!"  # 변수 y에 "Hello, World!" 문자열을 할당한다.

# Comment
# 코드의 한 줄을 주석 처리한다.
# print("Hello, World!") 

# Python Comments
# 한 줄 주석
print("Hello, World!")  # 한 줄 끝에 주석을 작성한다.

# Multiline Comments
"""
안녕하세요
감사합니다
잘 부탁드립니다
"""
print("Hello, World!")  # 여러 줄에 걸친 주석을 작성한다.

## Python Variables
# 변수에 값을 할당한다.
x = 10
y = "HoYoung"
print(x)
print(y)

# 다른 유형으로 변수를 설정한다 (int : 정수형 , str : 문자열)
x = 5       # 정수형으로 작성된 변수
x = "Sally" # 문자열로 작성된 변수
print(x)

# 문자열, 정수형, 실수형 등 원하는 데이터 유형으로 지정할 수 있다.
x = str(3)    # x는 '3'이 다.
y = int(3)    # y는 3이 된다.
z = float(3)  # z는 3.0이 된다.
print(type(x))
print(type(y))
pri한다.
# 숫자의 경우 + 문자는 수학 연산자로 작동한다.
x = 2
y = 3
print(x + y)

# 함수에서 print() 문자열과 숫자를 + 연산자와 결합하려고 하면 Python에서 오류를 표시한다.
x = 5
y = "John"
print(str(x) + y)

# 함수에서 여러 변수를 출력하는 가장 좋은 방법은 print() 변수를 쉼표로 구분하는 것이다.
x = 7
y = "HoYoung"
print(x, y)

## Python Data Types
# 데이터 유형을 가져온다.
x = 5
print(type(x))

## Python Numbers
# 숫자 유형에는 정수(int), 실수(float), 복소수(complex)가 있다.
# 한 유형에서 다른 유형으로 변환할 수 있다.
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
# 문자열 유형은 작은따옴표나 큰따옴표로 묶인다.
# 변수에 문자열을 할당한다.
a = "고마워"
print(a)

# 문자열 요소에 액세스한다.
a = "안녕, 반가워"
print(a[1])

# 문자열을 반복하여 출력한다.
for x in "catia":
    print(x)

# 문자열 길이를 출력한다.
a = "Hello, World!"
print(len(a))

# 문자열 검사
txt = "안녕하세요, 반갑습니다"
print("고마워요" not in txt)

txt = "안녕하세요, 반갑습니다"
if "고마워요" not in txt:
    print("No, '고마워요' is NOT present.")
