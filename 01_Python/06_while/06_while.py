#반복문 :
#1. for - in 다음에 반복할 범위를 지정
# range() 몇번 범위 -> 반복의 횟수(범위)가 정해져있다.
#for 변수 in 범위:
    #반복문장들

#2. while - 무한루프 -> 반복의 횟수가 정해져 있지 않고,
                    #조건이 만족하는 동안 반복한다.

#반복에 사용되는 변수를 초기화
#while 조건식:
    #반복할 문장들
    #반복을 빠져나가는 문장: 반복에 사용되는 변수의 값을 변화(증감식)

#무한루프
#while True:
#while = 1:
#while 변수명:
#while 조건식이 항상 참:

#break : 반복문을 빠져나옴
#continue : 그 다음 반복으로 진행

#1. 문제1: 1부터 10사이의 숫자 출력

#for
for num in range (1,11):
    print(num, end=' ')

#while문
num = 1
while num <= 10:
    print(num, end=',')
    num += 1 #num = num + 1

#2. 문제2: 1부터 100사이의 3배수들의 합 출력
#code1 - for 함수 사용
total = 0
for num in range (3,101,3):
    total += num
print('1~100사이의 3배수의 합:', total)

#code2 - while 함수 사용
total = 0
num=1
while num <= 100:
    if num % 3 ==0:
        total += num #합계구하기 total = 0 잡아주기
    num += 1 #num = 1 잡아주고, num은 1씩 커진다
print('1~100사이의 3배수의 합:', total)

#code3
total = 0
num = 3
while num <= 100:
    total += num
    num += 3
print('1~100사이의 3배수의 합', total)

#3. 문제3: 7을 입력할 때 까지 계속 입력하는 프로그램
num = int(input('숫자 입력:'))
while num != 7:
    num = int(input('숫자 재입력:'))
print('7 입력, 종료!')


#4. 문제4: if 1번 문제 - 십진수를 이진수로 변환
#code1 - 정석적인 방법
num = int(input('십진수 입력:'))
print(bin(num))

#code2
num = int(input('십진수 입력:'))
print(f'이진수 변환:0b{num:b}')

#code3 - while 함수 사용
num = int(input('십진수 입력:'))
bin='' #문자열 지정. bin을 0 숫자로 지정하면 111을 더해버려서 3이 나옴
while num > 0:
    rest = num % 2 #나머지
    num //= 2 #몫 - num = num // 2 (십진수를 계속 2로 나눠줌)
    bin += str(rest) #bin = str(rest) + bin -> 나머지 계속 붙이기
print('0b'+ bin)
