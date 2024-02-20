#Day2: 자료형과 연산자
# 1. 자료형(Data Type)

#기본 자료형: 정수(int), 실수(float), 부을(bool), 문자열(str)
#iterative / 집합적 자료형 / sequence : 리스트, 딕셔너리, 튜플, 세트

#1) 정수 진법 변환 함수
# 2진수, 8진수, 16진수, 10진수 -> 정수형
# bin(), oct(), hex()

#2진수로 변환
print('bin(123)=', bin(123)) #bin(123)= 0b1111011
print('bin(o123)=', bin(0o123)) #bin(o123)= 0b1010011
print('bin(123)=', bin(0x123)) #bin(123)= 0b100100011

#8진수로 변환
print('oct(123)=', oct(123)) #oct(123)= 0o173
print('oct(0o11010111)=', oct(0b11010111)) #oct(0o11010111)= 0o327
print('oct(0x123)=', oct(0x123)) #oct(0x123)= 0o443

print('hex(123)=', hex(123)) #hex(123)= 0x7b
print('hex(0o11010111)=', hex(0b11010111)) #hex(0o11010111)= 0xd7
print('hex(0o123)=', hex(0o123)) #hex(0o123)= 0x53

#변수의 자료형 : 실행할 때 결정(동적타이핑)
#id(), type()

#2) 형변환 함수
#형변환 함수: int(, base=10), float(), string()
#int(string), float(string), str(number)

#2-1) int(string, base=10) 정수변환
#int(string) : 10진수가 기본임
#int(string, 2), int(string, 8), int(string, 16)

print('int("123")=', int('123')) #int('123')= 123
print('int(\'1010\',2)=',int('1010', 2)) #int('1010',2)= 10
#base=2 or 2 -> 이진수
#print("int('ff')=",int('ff')) -> 에러 (정수형이 아니라서)
# 에러 : NameError, TypeError(데이터 유형 잘못), ValueError(값이 잘못)
print("int('ff', 16)=", int('ff', 16)) #int('ff', 16)= 255
print('int(\'123\', 8)=', int('123', 8)) #int('123', 8)= 83

#2-2) float(string): 문자열을 실수형으로 변환

print("float('13.5')=", float('13.5')) #float('13.5')= 13.5
print("float('13')=", float('13')) #float('13')= 13.0

#2-3) str(숫자): 문자열 변환

#print('나이는 = %d'%'20') #Type Error
print('나이는 = %d' % int('20'))
#print('나이는 =' + 20)-> Type Error '+'에서는 같은 타입 와야함
print('나이는 ='+ str(20))

#input() 함수: 키보드로 값을 입력 받아서 문자열로 반환
#input(prompt) : prompt는 화면에 표시되는 문자열
#괄호가 붙어있으면 무조건 함수
'''
name = input('이름: ')
year = int(input('출생연도: '))
print(f'이름은 {name} 나이는 {2024-year}')

num = float(input('실수입력: '))
result = num*10
print(f'{num}*10={result}')
'''

#2. 연산자 : *, + 등
#() [] {}
#부호: + -
#산술 * / % // ** + -      divmod()  pow()
#비트  ~ & ^ | >>  <<
#대입 = += -= //=
#관계 == != > < >= <=  : True False
#논리 and or not

# 단항연산자,  이항연산자, 삼항연산자
# -10  ~     3+10      a>>2

#print() input()
#대입 연산자: 왼쪽(변수) = 오른쪽(리터럴, 변수, 식, 함수...)


#SW => data + algorithm
# 문자열 + 문자열 = 두 문자열을 연결
# 문자열 * 숫자 = 문자열을 숫자만큼 생성해서 연결(반복)
#순차적 수행 / 제어문 (선택/반복)

sw = 'data ' + 'algorithm'
print(sw)

sw= 'data '*10
print(sw)


#연습문제 1. 두 정수를 입력 받아서 합계 출력
#num1 = int(input('정수 입력: '))
#num2 = int(input('정수 입력: '))
#print(f'합계는 {num1+num2} 이다')

num1 = int(input('정수1 입력:'))
num2 = int(input('정수2 입력:'))
print(f'합계는 {num1+num2}이다')

#연습문제 2. 몸무게와 키의 값을 입력받아서 BMI 지수 계산
#BMI = 몸무게 / 키(m)의 제곱

wgt = float(input('몸무게(kg) 입력:'))
hgt = float(input('키(m) 입력:'))
print(f'당신의 BMI: {wgt/(hgt**2):.2f}')
#f string 포맷함수: {변수: .2f} 소숫점 둘째 자리까지

#eval() 함수 : 값에 따라 변환

#산술연산자
print(pow(3,2)) # pow(3,2) -> 3에 2승
print(divmod(10,3)) #divmod(10,3) -> 몫, 나머지 계산

#연습문제 3. 예금액과 이자율을 입력받아서
#예금액, 이자율, 예금이자, 잔액 출력

m = float(input('예금액(원) = '))
ir = float(input('이자율(%) = '))
print(f'예금액:{int(m)}원, 이자율:{int(ir)}%, 예금이자: {int(m*ir/100)}원, 잔액:{int(m+(m*ir/100))}원')


#format 함수 (숫자, '숫자서식')
print(format(15000, ',.2f'))
print(format(15000, ',d'))


#3. if 문
#if 조건식
#if ~ else
#if ~ elif ~else


