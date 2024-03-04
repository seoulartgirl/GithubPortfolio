#재귀함수(recursive function)
#함수 내부에서 자신의 함수를 다시 호출

#1~n까지의 합 구하기
def sum(n):
    if n == 1:
        return 1
    return n+ sum(n-1)
print(sum(10))
#결과: 55

# 1*2*...*n : n! 계산하는 재귀함수

def fact1(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(fact1(5)) #결과: 120

def fact2(n):
    if n == 1:
        return 1
    return n * fact2(n-1)
print(fact2(5)) #결과: 120

#내부함수

def outFunc(x,y):
    def inFunc(a,b):
        return a+b
    return inFunc(x,y)

print(outFunc(10,30)) #결과: 40


#람다(lamda) 함수
#한줄짜리 함수, return문을 사용하지 않음
#변수명(함수이름) = lambda <인수들>:<반환할식>
#람다함수는 함수 참조(주소)를 반환
#변수로 람다함수 객체를 받아서 함수호출한다

f = lambda:1
print(f()) #결과: 1

add = lambda x,y:x+y
print(add(2,3)) #결과: 5

add = lambda x,y=10:x+y #디폴트 매개변수
print(add(2)) #결과: 12

add = lambda x=30,y=10:x+y
print(add()) #결과: 40
print(add(10)) #결과: 20
print(add(50,20)) #결과: 70
print(add(y=200,x=20)) #결과: 220

#람다 표현식 : 함수이름 명명하지 않고(변수에 할당하지 않고) 바로 호출
# (lamda <매개변수들>:식)(인수들)

#방법1) 변수에 할당
f = lambda x : x+10
print(f(10)) #결과: 20

#방법2) 함수 이름 명명하지 않고 호출
print((lambda x : x+10)(10)) #결과: 20

#람다표현식 안에서는 변수생성 불가
#(lambda x : y=10; x+y)(10) #syntaxError
y=10
(lambda x: x+y)(10)

(lambda x,y,z: x+y)(10,20,30)

def plus_ten(x):
    return x + 10
#[1,2,3,4,5] +10씩 더하고 싶으면
new=[]
for n in [1,2,3,4,5]:
    new.append(n+10)
print(new)
#결과: [11, 12, 13, 14, 15]

lambda x:x+10
print(map(list(plus_ten, [1,2,3,4,5])))
#결과: [11, 12, 13, 14, 15]

#람다 사용
print(list(map(lambda x:x+10, [1,2,3,4,5])))
#결과: [11, 12, 13, 14, 15]

# 두 개의 리스트 요소 더하기

def add_list(x, y):
    new_list = []
    for i in range(len(x)):
        new_list.append(x[i]+y[i])
    return new_list

a = [1,2,3,4]
b = [10,11,12,13]
print(add_list(a,b))
#결과: [11, 12, 13, 14, 15]

# map(func, iterable_data)함수
def add_two(x,y):
    return x+y

print(list(map(add_two, 1, 3)))
print(list(map(lambda x,y:x+y, 1, 3)))