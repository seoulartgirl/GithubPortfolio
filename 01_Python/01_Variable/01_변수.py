#Day1: 변수에 대해 실습

#1.변수(variable)
#변수란 데이터를 저장하는 메모리 주소
#파이썬에서는 변수선언 필요없음 (자바에선 int X; float X; 선언해야함)
#파이썬의 변수: 동적 타이핑(x는 어떤 변수든 다 들어갈 수 있음), 레퍼런스

#변수(variable) vs 함수(function)
#함수는 대문자로 시작/ 소괄호가 붙어있음/ .이 있으면 method(메소드)
#컴파일 언어: 소스파일(.java)->목적파일로 컴파일->실행파일(.exe)

#id() - 주소(숫자로 나옴), type() - 타입
#print(): 출력
#print()의 print는 식별자
#출력가능: 키워드, 연산자(덧셈, 뺄셈 나눗셈 등), 자료 등

#del -> delete
#True는 숫자로 할 때 1이 됨
#snake case(언더스코어) vs Camel Case (대소문자)

#1) 실습1: 두 변수의 값 교환 (Swap)

a=10
b=5
print(a,b)

#방법1: 고전적 방식
temp=a
a=b
b=temp

print(a,b)

#방법2: 파이썬 방식

a,b=10,5
print('a=', a, 'b=', b)
a,b=b,a
print('a=',a, 'b=', b)


#2) 실습2: 변수 삭제
#del a 삭제
#print(a)
#NameError 뜸

#3) 실습3: 변수의 값 출력 print()
age=30
name = 'HongGilDong'
print(name, age)

addr='서울시 서초구'
result = name + "은 " + addr + '에 살아요'
print(result)

print(name + ": 나이는 " + str(age)+ '입니다')
#TypeError: 문자열과 숫자는 연결할 수 없다
#숫자를 문자열로 변환하는 함수 활용: str(숫자)


#4) 실습: 변수를 이용한 계산 결과값 출력
#삼각형의 넓이 계산하여 출력

w=10
h=5
tot=(w*h)/2
print('넓이=', tot)

#print() 함수의 다양한 출력
#print('문자열', 변수)

#2. 포맷 서식
#1) 방법1: '서식'%값
#format code: %f(float실수-소수점o), %d(integer정수-소수점X)
#%s값(string 문자열), %x (hexadecimal 16진), %o(Octal 8진) %c, %% 등

print('넓이=%d'%tot)

# result1 = '%s은 %s에 살고 나이는 %d에요'%(name, addr, age)
# print(result1)
print('%s는 %s에 살고 나이는 %d에요'%(name, addr, age))

# result2 ='넓이=%.2f'%tot
# print(result2)
print('넓이=%.2f'%tot)

pcnt = 10.5
# result3= '전체면적의 %.3f%%입니다'%pcnt
# print(result3)
print('전체면적의 %.3f%%입니다'%pcnt) #퍼센트: %% 두개 붙여주기

#2) 방법2: format() 함수
#format(숫자, '숫자서식')

print(format(tot, '.2f'))
print(format(100, '5d'))

#연습문제:다음 변수 값들을 이용해 총점, 평균을 계산해 예시와 같이 출력하기

kor = 90
eng = 80
math = 75

#총점: 245, 평균 81.66

#code1
tot = format(kor + eng + math, 'd')
avg = format((kor + eng + math) / 3, '.2f')
print('총점:', tot, ', 평균:', avg)

#code2
tot=kor+eng+math
avg=format(tot/3, '.2f')
print('총점:', tot, ', 평균:', avg)

#code3
print('총점 : %d, 평균 : %.2f' %(kor+eng+math, (kor+eng+math)/3))


#3) 방법3: '{0:서식} {1:서식} {2:서식} .format( , , )함수
#str.format() 함수
print(format(3.141592, '10.3f'))
print('{0:.3f}'.format(3.1415927))
print('{1:5d} {2:05d} {0:.3f}' .format(kor, math, eng))


#4) 방법4: f'string => 3.6버전 부터 제공***
result5= f'수학점수는 {math:05d}점이고, 국어점수는 {kor:7.3f}점, 영어점수는 {eng}점입니다.' 
print(result5)
print(f' {math:05d} {kor:7.3f} {eng} ')


#print(int( )) -> int는 실수를 정수형으로 변환
balance = 10300.0
print(balance)
print(int(balance))
print(format(int(balance), ',')) #10300 -> 10,300 변환

#0b -> 이진수
#0b1011 -> 11
#0b10000000 -> 128
#0b11111111 -> 255
#0b111-> 7
#0b21-> SyntaxError -> 이진수에서 0은 없음
#0o7-> 7
#0o17-> 15
#0b001111 -> 15

#3. 상수(constant): 고정된 변수
# 파이썬에서 상수는 변수와 구분하지 않지만, 상수로 사용 가능
# 상수로 사용할 때 이름은 대문자로 표기할 것을 권장

#4. 리터럴 : 값 그 자체, 실수, 정수, 문자열, None, True, False

#5. print()함수의 매개 변수 활용
#sep='' / end =''
print('국어', kor, '수학', math, '영어', eng, end='====')
print('국어', kor, '수학', math, '영어', eng, sep='*')
#end에는 \n 이 들어가 있음 sep에는 띄어쓰기 들어가있음 ' '

#예제
print("%d/%d=%d"%(10, 4, 10/4)) #결과: 10/4=2
print("%d/%d=%f"% (10, 4, 10/4)) #10/4=2.500000
print("%d/%d = %5.1f"% (10, 4, 10/4)) #10/4 =   2.5
print("%d/%d=%5.0f"% (10, 4, 10/4)) #10/4=    2
print("%10s"%"파이썬") #       파이썬
print("%1.1f"% 123.45) #123.5

# 파이썬 Doc 사이트 : https://docs.python.org/3/index.html
# 내장함수(built-in functions) :
#      https://docs.python.org/3/library/functions.html
# 튜토리얼 : https://docs.python.org/3/tutorial/index.html
