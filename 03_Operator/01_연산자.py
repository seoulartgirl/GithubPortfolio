#연산자

#단항연산자 : -10
#이항연산자 : 3+10, a>>2
#삼항연산자
#구글링-ascii 코드표 참고

#1. 산술연산자 : +, -, *, /, %, //, **
#divmod(x,y): x를 y로 나눈 몫과 나머지 반환
#pow(3,2) : 3에 2승

#문제1. 10000초는 몇분 몇초인가?

#code1 - divmod 함수 사용
print(divmod(10000, 60)) #(166, 40)

#code2 - divmod 함수 사용 x
time = 10000
s = time % 60
m = time / 60
print(f'{int(m)}분 {s}초')

#문제1(변형). 10000초는 몇시간 몇분 몇초인가?

#code1
time = 10000
h = time // 60 // 60
m = time / 60 - h*60
s = time % 60
print(f'{h}시간 {int(m)}분 {s}초')

#code2
time = 10000
h=time//3600
#3600으로 나눈 time으로 재정의
time=time%3600
m= time//60
s=time%60
print(f'{time}초는 {h}시간 {m}분 {s}초 입니다.')

#code3 - divmod 함수 사용
time, second = divmod(10000, 60)
hour, min = divmod(time, 60)
print(hour, min, second)


#2. 관계연산자 : 두개의 논리값 크기비교 >, <, >=, <=, ==, !=

a=100
b=5
print(a==b) #False
print(f'{a}=={b}의 결과는 {a == b}') #False
print(f'{a}!={b}의 결과는 {a != b}') #True
print(f'{a}>{b}의 결과는 {a > b}') #True
print(f'{a}<{b}의 결과는 {a < b}') #False

#3. 논리연산자: and or not

print(a>200 and b<300) #False
print(a>10 and a<300) #True
print(not(a>200)) #True

#4. 비트연산자: &, |, ^, ~, <<, >>
# & - 비트 논리곱 (and) : 둘다 1인 경우에 1
# | - 비트 논리합 (or) : 한쪽만 1이라도 1
# ^ - 비트 논리적 배타합(xor) : 둘다 같으면 0, 다르면 1
# ~ 비트 부정: 1은 0으로, 0은 1로 변경
# << 비트 이동 (왼쪽): 비트를 왼쪽으로 시프트
# >> 비트 이동 (오른쪽): 비트를 오른쪽으로 시프트

a=100
b=5
print(f'~a: {~a}') #-101
print(f'a의 음수값: {~a+1}') #해당 값의 음수 값을 찾기 위해 사용
print(f'b<<1 : {b<<1}') #10 / 왼쪽 시프트 연산자: 값에 2에 n승을 곱한 효과
print(f'b<<3 : {b<<3}') #40
print(f'b>>1 : {b>>1}') #2 / 오른쪽 시프트 연산자: 값에 2에 n승을 곱한 효과
print(f'b>>2 : {b>>2}') #1
print(f'a>>3 : {a>>3}') #12

# 대입(할당) 연산자 : =

# 대입연산자 : +=, -=, *=, /=, //=, %=

print('a=', a)
a+=10 #a = a+10으로 재정의
print('a+=10 :', a )


#문제2. 지폐교환기
#지폐를 입력하면 50000, 10000, 5000, 1000원, 나머지로 환산

#code1
money = int(input('금액 입력(원):'))
fifty = money // 50000
ten = money % 50000 // 10000
five = money % 50000 % 10000 // 5000
one = money % 50000 % 10000 % 5000 //1000
rest = money % 50000 % 10000 % 5000 % 1000

print(f'5만원:{fifty}, 1만원:{ten}, 5천원:{five}, 1천원:{one}, 나머지:{rest}')


#code2 - divmod 함수 사용
money = int(input('금액 입력(원):'))
fifty, money = divmod(money, 50000)
ten, money = divmod(money, 10000)
five, money = divmod(money, 5000)
one, rest = divmod(money, 1000)

print(f'5만원:{fifty}\n1만원:{ten}\n5천원:{five}\n1천원:{one}\n나머지:{rest}')

#code3 - 대입연산자 활용 (+=)
money = int(input('금액 입력(원):'))
fifty = money // 50000
money %= 50000
ten = money // 10000
money %= 10000
five = money // 5000
money %= 5000
ten = money // 1000
money %= 1000
rest = money % 1000

print(f'5만원:{fifty}\n1만원:{ten}\n5천원:{five}\n1천원:{one}\n나머지:{rest}')

#code4
tot=int(input('금액 입력: '))
print(f'5만원: {tot//50000}장')
tot%=50000
print(f'만원: {tot//10000}장')
tot%=10000
print(f'5천원: {tot//5000}장')
tot%=5000
print(f'천원: {tot//1000}장')
tot%=1000
print(f'나머지: {tot}원')
