#문제1-1:다음 코드의 실행 결과를 쓰시오.
def test(t):
    t=20
    print("In Function:", t)

x =10
print("Before:", x)
test(x)
print("After:", x)

#결과:
#Before: 10
#In Function: 20
#After: 20


#문제1-2:다음 코드의 실행 결과를 쓰시오.
def sotring_function(list_value):
    return list_value.sort()
print(sotring_function([5,4,3,2,1]))

#결과: None

def sotring_function(list_value):
    return sorted(list_value)
print(sotring_function([5,4,3,2,1]))


#문제1-3:다음 코드의 실행 결과를 쓰시오.
number = "100"
def midterm(number):
    result = ""
    if number.isdigit() is True:
        if number == 100:
            if number/10 == 1:
                result = True
    else:
        result = False

    return result

#결과:
#False는 불린 타입인데 문자열("")로 정의되어 있어서?


#문제1-4:다음 코드의 실행 결과를 쓰시오.
def add_and_mul(a,b,c):
    return b + a * c + b
print(add_and_mul(3,4,5)==63)

#결과: False
# 23 != 63


#문제1-5:다음 코드의 실행 결과를 쓰시오.
def args_test_3(one, two, *args): #three하면 에러남
    print(one+two+sum(args))
    print(args)
args_test_3(3,4,5,6,7)

#결과: 25 / (5,6,7)


#문제1-6:다음 코드의 실행 결과를 쓰시오.
def rain(colors):
    colors.append("purple")
    colors = ["green", "Blue"]
    return colors

rainbow = ["red", "orange"]
print(rain(rainbow))

#결과: ["green", "Blue"]

#문제1-7:다음 코드의 실행 결과를 쓰시오.
def function(value):
    print(value ** 3)
print(function(2))

#결과: 8 / None 나오는 이유?


#문제1-8:다음 코드의 실행 결과를 쓰시오.
def get_apple(fruit):
    fruit = list(fruit)
    fruit.append("e")
    fruit = ["apple"]
    return fruit

fruit = "appl"
get_apple(fruit)
print(fruit)

#결과: appl
# global local

#문제1-9:다음 코드의 실행 결과를 쓰시오.
def return_sentence(sentence, n):
    sentence += str(n)
    n -= 1
    if n < 0:
        return sentence
    else:
        return(return_sentence(sentence, n))

sentence = "I Love You"
print(return_sentence(sentence,5))

#결과: I Love You543210

#문제1-10:다음 코드의 실행 결과를 쓰시오.
def test(x,y):
    tmp = x
    x = y
    y = tmp
    return y.append(x)

x = ["y"]
y = ["x"]
print(test(x,y))
print(y)

#결과: ["x"] / ?

#문제1-11:다음 코드의 실행 결과를 쓰시오.
def countdown(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
        countdown(n-1)
countdown(3)

#결과:
# Odd
# Even


#문제1-12:다음 코드의 실행 결과를 쓰시오.
def exam_func():
    x = 10
    print("Value:", x)

x = 20
exam_func()
print("Value:", x)

#결과:
# Value: 10
# Value: 20


#문제1-13:다음 코드의 실행 결과를 쓰시오.
def message():
    print("A")
    print("B")
message()
print("C")
message()

#결과: A / B / C / A / B


#문제1-14:다음 코드의 실행 결과를 쓰시오.
print("A")

def message():
    print("B")
print("A")
print("C")
message()

#결과: A / A / C / B


#문제1-15:다음 코드의 실행 결과를 쓰시오.
def message1():
    print("A")
def message2():
    print("B")
    message1()
message2()

#결과: B / A


#문제1-16:다음 코드의 실행 결과를 쓰시오.
print("A")
def message1():
    print("B")

print("C")
def message2():
    print("D")

message1()
print("E")
message2()

#결과: A / C / B / E / D


#문제1-17:다음 코드의 실행 결과를 쓰시오.
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range(3):
        message2()
        print("C")
    message1()
message3()

#결과: B / C / B / C / B / C / A


#문제1-18:다음 코드의 실행 결과를 쓰시오.
def calc_rect_area(width, height):
    width = 3
    height = 5
    result = width * height
    return result

width = 2
height = 4
#print(calc_rect_area(width, height))

#결과: 아무것도 출력 안됨

#문제1-19:다음 코드의 실행 결과를 쓰시오.
country = ["Korea", "Japan", "China"]
country.append("Remove")
print(country.remove("Remove"))

#결과 : None

#문제2: 다음 코드를 실행하면 결과값으로 120이 나온다. 빈칸에 들어갈 알맞은 코드를 작성하시오.
def factorial_calculator(n):
    if n in (0,1):
        return 1
    else:
        return n * 24
print(factorial_calculator(5))

#정답: 24

#문제3: 다음 코드에서 에러가 발생하는 이유는?
# hello()
# def hello():
#     print("Hi")

#수정 코드
def hello():
    print("Hi")

hello()
#print(hello()) # None이 나옴


#문제4-1: 다음 조건에 맞는 코드들을 작성하시오.
#"비트코인" 문자열을 화면에 출력하는 print_coin() 함수 정의
#문제4-2: 다음 조건에 맞는 코드들을 작성하시오.
# 1)에서 정의한 함수 호출
# def print_coin():
#     print("비트코인")
#
# print(print_coin())

#문제4-3: 다음 조건에 맞는 코드들을 작성하시오.
# 1)에서 정의한 함수 100번 호출
# for i in range(99):
#     print(print_coin())

#문제4-4: 다음 조건에 맞는 코드들을 작성하시오.
# "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수 정의
# (조건. 한 줄에 "비트코인" 문자열을 하나씩 출력)

def print_coin():
    print("비트코인")
    return

# for i in range(9):
#     for letter in list(result):
#         print(letter)

#문제4-5: 다음 조건에 맞는 코드들을 작성하시오.
# 두 수를 인자로 입력 받아 곱한 후 그 결과를 반환하는 mul() 함수 정의

def mul(x,y):
    return x*y
print(mul(2,3))


#문제4-6: 다음 조건에 맞는 코드들을 작성하시오.
# 소문자 문자열을 인자로 받아 대문자로 변환하여 반환하는 toUpper() 함수 정의
def toUpper(letter):
    return letter.upper()
print(toUpper('abc'))


#문제4-7: 다음 조건에 맞는 코드들을 작성하시오.
# 리스트를 인자로 받아 짝수만 모아 반환하는 pickup_even() 함수 정의
#code1
def pickup_even(list):
    list1 =[]
    for i in range (len(list)):
        if list[i] % 2 == 0:
            list1.append(list[i])
    return list1

list2 = [1,2,3,4,5,6]
print(pickup_even(list2))

#code2
def pickup_even(numbers):
    return [number for number in numbers if number % 2 == 0]

list2 = [1, 2, 3, 4, 5, 6]
print(pickup_even(list2))