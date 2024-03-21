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
해당 문장은 파이썬의 for 루프를 사용하여 과일 목록을 반복하는 것을 설명하고 있습니다. 여기에는 변수 x를 사용하여 반복하면서 과일 목록에 있는 각 항목을 출력하는 예시가 포함되어 있습니다.

python
Copy code
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
위 코드는 fruits 리스트의 각 항목("apple", "banana", "cherry")을 하나씩 반복하며 각 항목을 출력합니다.

해당 문장은 함수를 만들고 그 함수를 호출하는 방법을 설명하고 있습니다.

먼저, 함수를 만들기 위해서는 def 키워드를 사용합니다. 그리고 함수 이름을 정의하고, 함수의 동작을 작성합니다.

python
Copy code
def my_function():
    print("Hello from a function")
이제 만든 함수를 호출하려면 함수 이름 뒤에 괄호를 붙입니다.

python
Copy code
my_function()
이제 위의 코드를 실행하면 "Hello from a function"이라는 메시지가 출력됩니다.
해당 문장은 람다 함수에 대한 설명과 예제를 제공하고 있습니다.

람다 함수는 작고 익명의 함수입니다. 람다 함수는 임의의 개수의 인수를 취할 수 있지만 오직 하나의 표현식만을 가질 수 있습니다.

람다 함수의 구문은 다음과 같습니다:

python
Copy code
lambda 인수 : 표현식
표현식이 실행되고 결과가 반환됩니다.

예를 들어, 아래의 코드는 인수 a에 10을 더하고 결과를 반환하는 람다 함수를 정의하고 사용하는 예제입니다:

python
Copy code
x = lambda a: a + 10
print(x(5))
위 코드를 실행하면, 5에 10을 더한 결과인 15가 출력됩니다.

람다 함수는 임의의 개수의 인수를 취할 수 있습니다. 아래의 예제는 인수 a와 b를 곱하고 결과를 반환하는 람다 함수를 보여줍니다:

python
Copy code
x = lambda a, b: a * b
print(x(5, 6))
위 코드를 실행하면, 5와 6을 곱한 결과인 30이 출력됩니다.

이와 같이 람다 함수를 사용하면 익명 함수를 간단하게 정의하고 사용할 수 있습니다.

파이썬에서 배열을 사용하는 방법을 리스트로 구현하는 방법을 안내하고 있습니다. 그러나 파이썬에서 배열을 다루기 위해서는 NumPy와 같은 라이브러리를 가져와야 합니다.

배열은 하나의 변수에 여러 값을 저장하는 데 사용됩니다.

python
Copy code
cars = ["Ford", "Volvo", "BMW"]
배열이란?
배열은 한 번에 하나 이상의 값을 저장할 수 있는 특별한 변수입니다.

아이템 목록(예: 자동차 이름 목록)이 있다고 가정해 보겠습니다. 이를 개별 변수에 저장하는 방법은 다음과 같을 수 있습니다.

python
Copy code
car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"
그러나 자동차를 순회하고 특정 자동차를 찾으려면 어떻게 해야 할까요? 그리고 만약 자동차가 3대가 아니라 300대였다면 어떨까요?

해결책은 배열입니다! 배열은 하나의 이름으로 많은 값을 저장할 수 있으며 인덱스 번호를 사용하여 해당 값에 액세스할 수 있습니다.

배열의 요소에 접근하기
인덱스 번호를 참조하여 배열 요소에 액세스할 수 있습니다.

python
Copy code
x = cars[0]
배열의 길이
len() 메서드를 사용하여 배열의 길이(배열의 요소 수)를 반환할 수 있습니다.

python
Copy code
x = len(cars)
배열 요소 순환
for in 루프를 사용하여 배열의 모든 요소를 순회할 수 있습니다.

python
Copy code
for x in cars:
  print(x)
배열에 요소 추가
append() 메서드를 사용하여 배열에 요소를 추가할 수 있습니다.

python
Copy code
cars.append("Honda")
배열 요소 제거
pop() 메서드를 사용하여 배열에서 요소를 제거할 수 있습니다.

python
Copy code
cars.pop(1)
remove() 메서드를 사용하여 배열에서 요소를 제거할 수도 있습니다.

python
Copy code
cars.remove("Volvo")
배열 메서드
파이썬에는 리스트/배열에 사용할 수 있는 일련의 내장 메서드가 있습니다.

append(): 리스트 끝에 요소를 추가합니다.
clear(): 리스트에서 모든 요소를 제거합니다.
copy(): 리스트의 복사본을 반환합니다.
count(): 지정된 값과 일치하는 요소의 수를 반환합니다.
extend(): 리스트(또는 임의의 반복 가능한 항목)의 요소를 현재 리스트 끝에 추가합니다.
index(): 지정된 값과 일치하는 첫 번째 요소의 인덱스를 반환합니다.
insert(): 지정된 위치에 요소를 추가합니다.
pop(): 지정된 위치의 요소를 제거합니다.
remove(): 지정된 값과 일치하는 첫 번째 항목을 제거합니다.
reverse(): 리스트의 순서를 반전합니다.
sort(): 리스트를 정렬합니다.
파이썬에는 배열을 직접 지원하는 내장 기능이 없지만 파이썬 리스트를 대신 사용할 수 있습니다.
