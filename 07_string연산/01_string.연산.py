#1 문자열 생성

text = 'python is programming language'

#2. 문자열 인덱싱: [인덱스]

print(text[-1])
print(text[1])
print(text[11])

#3. 문자열 슬라이싱 [start:end] [start:end:step]
#부분 문자열 반환

print('text[2:10]:',text[2:10])
print('text[:]:', text[:])
print('text[::-1]:', text[::-1])
print('text[2:11:-1]:',text[2:11:-1])
print('text[2:11:-2]:', text[2:11:-2])
print('text[::2]:', text[::2])
print('text[2:]:', text[2:])

#4. 더하기 연산, 곱하기 연산, str(), len()
name ='kim'
age = 20
hi = 'hi!'
person = name + str(age)
print(person)

print(hi*5)

print('len(text):', len(text))

#5. 멤버 연산: in, not in

if 'python' in text:
    print('exist!')
else:
    print('not exist!')

if 'python' not in text:
    print('not exist!')
else:
    print('exist!')

# for의 in 연산에서 문자열 사용시 하나의 문자별로 작업
for p in text:
    print(p)

#입력 받는 문자열을 거꾸로 출력하기
text = input('문자열 입력:')
print(text[::-1])