#Day 3: 조건문 if
#조건문 if: 연습
#반복문 :
#  for - range() 몇번 범위  => 반복의 횟수(범위)가 정해져있다
#  for 변수 in 범위/대상:
#  반복문장들

#  while - 무한루프 조건
#  => 반복의 횟수가 정해져 있지 않고, 조건이 만족하는 동안 반복할 경우

#  반복에 사용되는 변수를 초기화
#  while 조건식:
#   - 반복할 문장들
#   - 반복문을 빠져나가는 문장 : 반복에 사용되는 변수의 값을 변화(증감식)

#무한루프
#  while True:
#  while 1:
#  while 변수명:
#  while 조건식이 항상 참:

#break : 반복문을 빠져나옴
#continue : 그 다음 반복으로 진행

#중첩 반복문
#for
#   for

#while
#   while

#for
#   while

#while
#   for

#반복문 for
#다중 for를 이용

#문제-------------------------------------

#1. 조건문 if
num=int(input('정수 입력:'))
if num > 10:
    print('10보다 크네요')

#if~else문
if num > 10:
    print('10보다 크네요')
else: #pass -> 그냥 pass 할 수도 있음
    print('10보다 작거나 같아요')


#연습문제1: 등록된 아이디, 비밀번호 확인 로그인

#code1
ID=input('아이디 입력:')
PW=input('비밀번호 입력:')

if ID == 'flower' and PW == '1234':
    print('로그인 성공!')
else:
    print('로그인 실패!')


#code2 - 아이디 or 비밀번호 오류를 나타내고 싶을 때
# 중첩 if: if 조건이 만족하는 경우 또 다른 조건 따라 실행
#if 아래에 if 존

ID = input('아이디 입력:')
PW = input('비밀번호 입력:')
if ID == 'flower':
    if PW == '1234':
        print('로그인 성공!')
    else:
        print('비밀번호 오류')
else: print('아이디 오류')

#code3 - 아이디 and 비밀번호 오류 까지 표기할때
#중첩 if: if 조건이 만족하는 경우 또 다른 조건 따라 실행
    #if 아래에 if 존
    #if~elif~else문 : 중첩 if
    #else if = elif

ID = input('아이디 입력:')
PW = input('비밀번호 입력:')
if ID == 'flower':
    if PW == '1234':
        print('로그인 성공!')
    else:
        print('비밀번호 오류')
elif PW == '1234':
    print('아이디 오류')
else:
    print('아이디, 비밀번호 오류')


#연습문제2: 점수 입력(0~100)받아서 학점 출력
#90점 :A
#80점 이상 90미만: B
#70점 이상 80점 미만: C
#60점 이상 70점 미만: D
#60점 미만: F

#code1
grade = int(input('점수 입력:'))
if grade >= 100 or grade < 0:
    print('숫자 0~100 사이로 입력해주세요')
if grade >= 90:
    print('A')
if 90 > grade >= 80:
    print('B')
if 80 > grade >= 70:
    print('C')
if 70 > grade >= 60:
    print ('d')
else: print('F')

#code2 - code1과 같으나 elif 함수 사용
grade=int(input("점수:"))
if grade >= 100 or grade < 0:
    print('숫자 0~100 사이로 입력해주세요')
elif grade>=90:
        print('A')
elif grade>=80:
        print('B')
elif grade>=70:
        print('C')
elif grade>=60:
        print('D')
else: print('F')