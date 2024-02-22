# 1. 문자열 정의 : 한줄, 여러줄
text1 = 'Python is great!'
text2 = "Yes, it is."
text3 = "It's not like any other"
text4 = 'Don\'t walk.'
text5 = 'This \n is \
contain \
temp'
print(text5)
text6 = """apple\n
banana
melon 
"""
print(text6)

#2. 문자열 포맷(서식) 지정
# 1) 포맷코드 '문자열 포맷코드' % (변수들)
#    '%05d %.2f %s %c ' % ( , , , )
print('%s는 %d살입니다' %('홍길동', 10))

#2) 문자열 {위치 인덱스}. format(변수)
# '{0:.2f}{2:5d}{1:s}'.format( , , )
name = 'kim'
age=20
print('{0}은 {1}살입니다'.format(name, age))

#     '문자열 {변수}'.format(변수=값)
print('{name}은 {age}살입니다'.format(name='홍길동', age=10))

# 3) format(변수, '서식' )
#    format(bmi, '.2f')

# 4) f'string : f' {변수 } {변수:서식 } '
print(f'{name}은 {age}살입니다.')

#3. 날짜 출력 포맷
# 주민번호 / 전화번호 / 우편번호 / 시간 / 날짜 /

# 모듈(module) : 함수나 변수를 모아 놓은 파일
from datetime import date, datetime, timedelta

today = date.today() #'.'은 소속을 나타냄 / 오늘의 날짜
print(today, type(today))
print(f'{today.year}년 {today.month}월 {today.day}일')
print(type(today.year))

#method : 메소드, field: 객체의 변수
curr_time = datetime.now().date()
curr_time = datetime.now().time()

print(curr_time)
print(curr_time, type(curr_time))

print(curr_time.hour, curr_time.minute, \
      curr_time.second, curr_time.microsecond)

#timedelta() 함수 :날짜 계산 용도로 사용
print(timedelta(days=-1))
print(timedelta(weeks=-1))
print(timedelta(hours=-1))

print(today + timedelta(days=-1))
print(today + timedelta(weeks=-1))

curr_time = datetime.now()
print(curr_time + timedelta(hours=-1))
print(curr_time + timedelta(days = 2, hours=4))

#strfrime() : 날짜, 시간 서식 지정
print(today.strftime('%Y-%m-%d %H:%M:%S'))
print(today.strftime('%y-%m-%d %I:%M:%S %p'))
print(curr_datetime.strftime('%y년%m월%d일 %I:%M:%S %p'))

#4. 문자열 정렬
# 왼쪽 정렬: <
# 오른쪽 정렬: >
# 가운데 정렬: ^
# 공백 문자 지정 : -

text = 'Python is great!'

print('{0:<20}'.format(text), 'end')
print(f'{text:>20}') #오른쪽으로 정렬해라

print('{0:^20}'.format(text), 'end')
print(f'{text:^20}') #가운데로 정렬해라

print('{0:*^20}'.format(text), 'end')
print(f'{text:#^20}') #공백 문자 '#, *' 지정

print('{0:#<20}'.format(text), 'end')
print(f'{text:>20}')
print('{0:*^20}'.format(text), 'end')
print(f'{text:#^20}')