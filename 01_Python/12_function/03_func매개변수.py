#함수의 매개변수(parameter)와 인수(인자:argument)

#1. 매개변수(parameter): 함수로 전달되는 값을 갖는 변수 (함수 정의)
#add(a,b) -> 매개변수 a,b
#인수/인자(argument): 함수를 호출할때 전달되는 값(변수)
#add(10,20) -> 인수 10,20

def get_area(width, height):
    result = width*height
    print(f'가로{width}, 세로{height}, 면적{result}')
    return result
print(get_area(10,20))

#결과: 가로10, 세로20, 면적200
# 200 -> return result 부분에 해당하는 결과값

#문제: 사칙 연산을 수행하는 함수 정의
#add(a,b): 두 수 더하기
#sub(a,b) : 뺄셈
#mul(a,b) : 곱셈
#div(a,b) : 나눗셈


x= 2
y= 0 #전역변수
def add(x, y):
    return x + y
print(f'{x}+{y}={add(x,y)}') #결과: 2+0=2

def sub(x, y):
    return x - y
print(f'{x}-{y}={sub(x,y)}') #결과: 2-0=2

def mul(x, y):
    return x * y
print(f'{x}*{y}={mul(x,y)}') #결과: 2*0=0

def div(x, y):
    if y == 0:
        print('0으로 나눌 수 없음') #결과: 0으로 나눌 수 없음
    else:
        return x / y
print(f'{x}/{y}={div(x,y)}') #결과: 2/0=None


#2. 디폴트 매개변수
#매개변수의 기본값이 지정되어 있는 경우
#디폴트 매개변수는 마지막에 위치해야 함

def greet(name,msg='hi'): #키워드 인수 -> 지정하는 것
    print(name + ',' + msg)
greet('hong') #결과: hong,hi

def greet(name,msg):
    print(name + ',' + msg)
greet('hong', 'hello') #결과: hong,hello


print('hi', end=' ')
print('hi', end='\n') #디폴트가 '\n'
#결과: hi hi

#3. 위치 매개변수(positional parameter)
#매개변수의 위치가 실인수로 전달받을 때 동일한 위치의 변수에 저장됨
#매개변수의 순서대로 인수를 전달

# def add(a,b)
#     pass
# add(3,5)

#4. 함수에 여러개의 자료(리스트, 딕셔너리) 전달
def show_names(names):
    for name in names:
        print(name, end='\n')
show_names(['홍길동', '심청이', '강감찬'])
#결과:
#홍길동
#심청이
#강감찬

def show_info(info):
    print(info)
    for key, value in info.items():
        print(key, info[key])
info = {'이름':'홍길동', '나이':20}
show_info(info)
#결과:
#{'이름': '홍길동', '나이': 20}
#이름 홍길동
# 나이 20

#5. 가변길이 매개변수
#매개변수의 길이가 정해지지 않는 경우 여러개의 값을 전달 받을 때 사용
# *args (arguments) , **kwargs (keyword arguments) : 딕셔너리의 key=value 형태로 값을 받음

print('hi', 'ho', sep=' ', end='\n')
#결과: hi ho

#1) *args 매개변수
def my_sum(a, b):
    return
my_sum(1,2)
#my_sum(1,2,3) 인자가 여러개 일때 오류가 남

def my_sum(*num):
    total = 0
    for n in num:
        total += n
    return total

print(my_sum(1,2,3,4,5,6,7)) #결과: 28

#2) *kwargs 매개변수
def info(**kwargs):
    for key in kwargs.keys():
        print(key, kwargs[key])

info(id='abc', name='hong')
# #결과:
# id abc
# name hong

def info(**kwargs):
    for key in kwargs.keys():
        print(key, end=' ')
    print() #띄어쓰기
    for value in kwargs.values():
        print(value, end =' ')
    print()
    for item in kwargs.items():
        print(item,  end='\n')
info(id='abc', name='hong', age=30)
#결과:
# id name age
# abc hong 30
# ('id', 'abc')
# ('name', 'hong')
# ('age', 30)

#6. 키워드 인수(keyword arguments)
# 인수들 앞에 키워드를 두어서 인수를 구별
# 인수의 위치가 매개변수의 위치와 달라도 됨
def my_print(a,b,c):
    print(a)
    print(b)
    print(c)
my_print(10,30,40) #결과: 10 / 30 / 40

my_print(a=5, b=10, c=30) #결과: 5 / 10 / 30
my_print(5, b=10, c=30) #결과: 5 / 10 / 30
# my_print(c=10, 30, 2) -> 오류 발생 / 뒤에서 부터 와야 함

#*args는 반드시 **kwargs 앞에 와야 함
def my_func(*args, **kwargs):
    pass

my_func(1,2,3, a=0, b=2)
my_func(1, a=10, b=3)

#밑에껀 오류 발생함 *args가 뒤로 가면 안됨
# def my_fun(**kwargs, *args):
#     pass

#함수 호출:
#위치 인수와 키워드 인수를 함께 사용하는 경우, 키워드 인수가 위치인수 뒤로
#함수 정의: 위치매개변수 뒤에 디폴트 매개변수는 뒤에
