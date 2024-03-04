#지역변수(local variable)와 전역변수(global variable)
#지역변수: 함수 내부에서 정의된 변수, 함수 안에서만 사용가능
#       함수 호출시 생성되고, 함수 종료되면 소멸되어 더 이상 사용 불가

a = 10 #전역변수
def show_info(name):
    age = 10 #지역변수 - 함수 밖에 영향을 줄 수 없음
    print(name, age)

show_info('hong') #결과: hong 10
#print(name) #NameError: name 'name' is not defined
#print(age) #NameError: name 'age' is not defined
#지역변수는 함수 안에서만 사용가능

a=10
def show1():
    a = 1 #지역변수 - 위 a와 이름은 같지만 다른 변수
    a = a+1
    print(a, id(a))
show1() #결과 2 4332588584
#지역변수명과 전역변수 이름이 같은 경우 지역변수가 우선한다.

def show2():
    a = a + 1     # 지역변수를 찾음: 오류 발생
    print(a, id(a))
# print(show2())
# UnboundLocalError: cannot access local variable 'a' where it is not associated with a value

def show3():
    b = a+1 #a: 전역변수
    print(a, id(a))
print(a, id(a)) #여기 a는 위에 정의된 a 전역변수
#결과: 10 4332588840 (id 값이 다름)

def show4():
    global a #전역변수 사용
    a = a + 1 #전역변수
    print(a, id(a))

show1() #결과: 2 4325150248
print(f'전역변수 a : {a}', id(a)) #결과: 전역변수 a : 10 4325150504


#예제
def sub(x,y):
    a=7
    x,y = y,x
    b=3
    print(a,b,x,y)

a,b,x,y=1,2,3,4
sub(x,y) #7,3,4,3 -> a,b는 지역변수
print(a,b,x,y) #1,2,3,4 -> a,b는 전역변수


#예제2
def sub(x,y):
    global b #전역변수를 함수 내부에서 사용/변경하고자 할때
    a=7
    x,y = y,x
    b=3
    print(a,b,x,y)

a,b,x,y=1,2,3,4
sub(x,y) #7,3,4,3 -> a,b는 지역변수
print(a,b,x,y) #1,3,3,4 -> a,b는 전역변수
#b가 3으로 바뀐 이유 -> global b=3 이것 지역변수 아님, 전역변수

def show_list(mylist):
    print(mylist, id(mylist))
mylist = [1,2,3,4]
show_list(mylist)
print(mylist, id(mylist))

#결과:
#[1, 2, 3, 4] 4302096640
#[1, 2, 3, 4] 4302096640

def show_list(mylist):
    cpy_list=mylist.copy() #함수 원본을 보존하고자 할 때 copy 함수 쓰기 / shallow copy
    cpy_list[-1] = 100
    print(cpy_list, id(cpy_list)) #[1, 2, 3, 100] 4371450112
mylist = [1,2,3,4]
show_list(mylist)
print(mylist, id(mylist)) #[1, 2, 3, 4] 4372003328