#1. 문제1: 정수를 입력 받아서 홀수, 짝수 인지 판별하여 출력
num = int(input('정수 입력:'))
if num % 2 == 0:
    print('짝수')
else:
    print('홀수')


#2. 문제2: 정수 3개를 입력 받아서 제일 큰 수 출력
#code1
num1 = int(input('숫자1 입력:'))
num2 = int(input('숫자2 입력:'))
num3 = int(input('숫자3 입력:'))
if num1 >= num2 and num1 >= num3:
    print('가장 큰 수:', num1)
elif num2 >= num3: #and num2 > num1 -> 안해도 되는 이유는 maxNum이 num1이 아니기 때문
    print('가장 큰 수:', num2)
else: print('가장 큰 수:', num3)

#code2
num1 = int(input('숫자1 입력:'))
num2 = int(input('숫자2 입력:'))
num3 = int(input('숫자3 입력:'))
max=0
if num1>=num2:
    max=num1
else: max=num2
if max >= num3:
    pass
else: max=num3
print(max)

#code3
num1 = int(input('정수1 입력 : '))
num2 = int(input('정수2 입력 : '))
num3 = int(input('정수3 입력 : '))

if num1 >= num2 >= num3:
    print('제일 큰 수:', num1)
elif num1 <= num2 <= num3:
    print('제일 큰 수:', num3)
else:
    print('제일 큰 수:', num2)


#3. 문제3: 도형(사각형, 삼각형, 원) 중 선택하여 해당되는 도형 면적 구하기
#사각형 : 가로, 세로 / 삼각형: 밑변, 높이 / 원: 반지름 (원의 면적은 반지름 제곱*3.14)
shape = int(input('도형 입력(1: 사각형, 2: 삼각형, 3: 원): '))
if shape == 1:
    w=float(input('가로:'))
    h=float(input('세로:'))
    print('사각형 면적:', '%.2f'%(w*h)) #format함수: '서식'%값 '%d'%tot
elif shape == 2:
    w=float(input('밑변:'))
    h=float(input('높이:'))
    print('삼각형 면적:', '%.2f'%(w*h/2))
elif shape == 3:
    r=float(input('반지름:'))
    print('원 면적:','%.2f'%(r**2*3.141592)) #format 소수 둘째 자리 까지
else: print('숫자 1~3 사이에서 골라주세요')


#4. 문제4: 컴퓨터와 주사위 놀이 하기
#주사위 눈의 숫자를 입력하면
#컴퓨터도 난수로 주사위 눈의 수를 발생시켜 게임 이긴 사람 출력
#주사위 눈의 수의 입력: 5
#컴퓨터가 이겼어요!
#축하합니다. 이기셨습니다!

#랜덤 숫자 생성 (난수)
from random import randint
randint(1,6)
#1~6 중 랜덤 숫자 선정됨

from random import randint
roll=int(input('주사위 눈의 숫자 입력(1-6):'))
pc=randint(1,6)

if roll>6 or roll<=0:
     print('잘못된 숫자를 입력했습니다')

if roll>pc:
    print('축하합니다. 이기셨습니다!')
elif roll==pc:
    print('무승부입니다')
else:
    print('컴퓨터가 이겼어요!')



#5. 문제5: 입력받은 십진수를 2진수로 변환하여 출력하는 프로그램 작성
#(파이썬에서 제공하는 bin()함수를 사용하지 말것)

#기본방식
print(bin(15)[2:]) #0b1111 # [2:] 사용하면 0b 없앨 수 있음
print(bin(10)) #0b1010
print(int('a', 16)) #10 ->16진수를 10진수로 변환하는 함수

#code1 - 십진수 입력: 15 / 10
num=int(input('십진수 입력:'))
bi_num = "{0:b}".format(num)
print(bi_num)

#code2
num=int(input('십진수 입력:'))
print(f'{num:b}') #f string 에서 bin형테로 출력


#6. 문제6: 16진수 글자 하나를 입력하면 16진수인지 아닌지를 구분하여
#16진수인 경우 10진수로 변환하여 출력하는 프로그램 작성

#code1 - 다 입력해야 해서 조금 비효율적
hex = ['a', 'b' ,'c' ,'d', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
word = input('16진수 한글자 입력:')
if word in hex:
    print('10진수:', int(word,16)) #16진수를 10진수로 변환
elif len(word) >=2: #두 자리 이상 입력시
    print('입력 가능한 글자 수를 초과하였습니다.')
else:
    print('16진수가 아닙니다.')

#code2 - 16진수 한 글자 입력 : f
num = input('16진수 한글자 입력:')
if len(num)>=2:
    print('입력가능한 글자 수를 초과하였습니다')
elif ('0' <= num <= '9') or ('a' <= num <= 'f') or ('A' <= num <='F'):
    print ('10진수:', int(num, 16))
else: print('16진수가 아닙니다')

#code3
num=input('16진수 한글자 입력 :')
if len(num) == 1:
    if "A" <= num <= "F" or "a" <= num <= "f" or '0'<= num <='9':
        print('10진수: ', int(num, 16))
    else:
        print('입력하신 ',num,'은 16진수 글자가 아닙니다')
else:
    print('한글자를 초과하여 입력하셨습니다')