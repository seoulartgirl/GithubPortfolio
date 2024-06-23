# 1. 문자열 생성

text = 'Python is programming language'

# 2. 문자열 인덱싱 : [인덱스]
print('text[-1] :',text[-1]) #e
print('text[1] :',text[1]) #y
print('text[11] :',text[11]) #r

#3. 문자열 슬라이싱 [start:end]  [start:end:step]
# 부분문자열 반환

print('text[2:11] :', text[2:11]) #thon is p
print('text[:] :', text[:]) #Python is programming language
print('text[::-1] :', text[::-1]) #egaugnal gnimmargorp si nohtyP
print('text[::-2] :', text[::-2]) #eaga nmagr inhy
print('text[::2] :', text[::2]) #Pto spormiglnug / 처음 ~ 끝까지 두칸씩
print('text[::11] :', text[::11]) #Prl / 처음 ~ 끝까지 두칸씩
print('text[2:] :', text[2:]) #thon is programming language

# 4. + 연산, * 연산, str(), len()
name = 'kim'
age = 20
hi ='hi!'
person = name + str(age)
print(person, type(person)) #kim20 <class 'str'>
print(hi*5) #hi!hi!hi!hi!hi!

print('len(text):',len(text)) #len(text): 30

#5. 멤버연산 : in, not in

if 'Python' in text:
    print('exist!')
else:
    print('not exist!') #exist!

if 'Python' not in text:
    print('not exist!')
else:
    print('exist!') #exist!

# for의 in 연산에서 문자열 사용시 하나의 문자별로 작업
for ch in text:
    print(ch)

#입력 받는 문자열을 거꾸로 출력하기
text = input('문자열 입력:')
print(text[::-1])
