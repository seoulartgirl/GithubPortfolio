# # 함수 정의 및 호출
# # 재사용 / 자주 사용하는 기능들을 위한 코드 집합
# # 경제적, 관리 용이
# # 내장 함수(built-in-fuction) / 사용자 정의 함수
# # https://docs.python.org/3.12/library/functions.html
#
# # 함수 정의 및 호출
#
# #예. 이름, 나이, 연락처 출력하는 함수
#
# def show_info():
#     print('이름: 홍길동')
#     print('나이:20')
#     print('연락처: 010-111-1111')
# show_info()
#
# #결과:
# # 이름: 홍길동
# # 나이:20
# # 연락처: 010-111-1111
#
#
# #나이, 이름, 연락처를 입력받아서 출력
# def show_info1():
#     name = input('이름 입력:')
#     age = input('나이 입력:')
#     phone = input('연락처 입력:')
#     print(f'이름: {name}')
#     print(f'나이: {age}')
#     print(f'연락처: {phone}')
#
# show_info1()

#문제. 두 정수를 입력받아 더하는 함수 add() 정의하기

def add():
    num1 = int(input('정수1 입력:'))
    num2 = int(input('정수2 입력:'))
    print(f'합계: {num1 + num2}')

print(add())

#결과: 합계: 3
# None -> 값이 없음
# None이 출력되는 이유는 return statement가 없어서


#반환 값이 있는 함수 정의
def add2():
    num1 = int(input('정수1 입력:'))
    num2 = int(input('정수2 입력:'))
    print(f'합계: {num1+num2}')
    return num1 + num2 #이렇게 하면 뒤에 None이 출력 안됨
print(f'return value = {add2()}') #합계값 한번더 출력됨

