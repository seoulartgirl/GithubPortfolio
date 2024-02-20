# 1. 문자열 생성

text = 'Python is programming language'

# 2. 문자열 인덱싱 : [인덱스]
print('text[-1] :',text[-1])
print('text[1] :',text[1])
print('text[11] :',text[11])

#3. 문자열 슬라이싱 [start:end]  [start:end:step]
# 부분문자열 반환

print('text[2:11] :', text[2:11])
print('text[:] :', text[:])
print('text[::-1] :', text[::-1])
print('text[::-2] :', text[::-2])
print('text[::2] :', text[::2])
print('text[:11] :', text[::11])
print('text[2:] :', text[2:])

# 4. + 연산, * 연산, str(), len()
name = 'kim'
age = 20
hi ='hi!'
person = name + str(age)
print(person, type(person))
print(hi*5)

print('len(text):',len(text))

#5. 멤버연산 : in, not in

if 'Python' in text:
    print('exist!')
else:
    print('not exist!')

if 'Python' not in text:
    print('not exist!')
else:
    print('exist!')

# for의 in 연산에서 문자열 사용시 하나의 문자별로 작업
for ch in text:
    print(ch)