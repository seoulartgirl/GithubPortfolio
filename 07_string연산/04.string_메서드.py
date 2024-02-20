#1. 문자열 대소문자 변환
#upper() #대문자화
#lower() #소문자화
#title() #제목, 단어별 시작문 대문자화
#capitalize() #문장의 처음만 대문자화

text1 = 'Python is great!'
text2= 'Yes, it is.'
text3 = "It's not like any other"

print('text1:', {text1})
print('text2:', {text2})
print('text3:' ,{text3})

print(text1.upper()) #대문자화
print(text2.lower()) #소문자화
print(text2.lower().title()) # 소문자화, 제목화
print(text1.upper().capitalize()) #대문자화, 첫글자 대문자

#2. 문자열 검색
#count(단어), find(단어), rfind(), index(), rindex()
print('count()', text1.count('Python'))

text4 = 'I like python, I like swimming, i like hotdog.'
print('count():', text4.count('like'))
print('find():', text4.find('like')) #인덱스 반환(첫번째로 만난 위치)
print('rfind():', text4.rfind('like'))
print('find():', text1.find('Python'))
print('find():', text1.find('melon'))
print('rfind():', text1.rfind('melon'))
print('index():', text4.index('like'))
#print('index():', text1.rindex('python')) #찾는 문자열 없으면 오류 발생
# print('startswith():', text4.startwith('I like')) #논리값 반환
# print('endswith():', text4.endswith('.')) #논리값 반환
# print('startswith():', text4.startwith('I like', 7)) #논리값 반환


#3. 문자열 치환, 편집
#strip(), rstrip() lstrip() : 공백문자(지정문자) 제거
#replace(): 문자 치환

text5 = '      ham haha hotdog!     '
text6 = '<><>hoho>>>>!'
print(text5.strip())
print(text5.lstrip())
print(text5.rstrip())
print(text6.strip('<>'))
print(text6.strip('>'))
print('replace():', text5.replace('ham', 'hom'))

#4. 문자열을 분리/결합
print(text4)
print('split():', text4.split())
print('split():', text4.split(','))
print('rsplit():', text4.rsplit())

text8 = 'apple banana kiwi'
data = text8.split
print(data)

text9 = '''firstline
secondline
thirdlind'''
print(text9.split())


#5. 문자열 정렬 : 포맷, ^ <>
#center(), ljust(), rjust()
print('center():', text8.center(30))
print('ljust()', text8.ljust(30, '-')) #왼쪽 정렬
print('rjust()', text8.rjust(30, '-')) #오른쪽 정렬

#6. 문자열 판단: 숫자, 알파벳, ...
#isdigit(), isdecimal(), isalpha(), ...
print('1234'.isdigit()) #True 숫자냐
print('abc한글'.isalpha()) #False 알파벳이냐
print('1234****'.isalnum()) #False
print('hello'.isupper()) #False 대문자
print('hello'.islower()) #True 소문자
print('hello'.istitle()) #False 제목

#unicode : \u0101 유니코드들
print('\u0101', '\u0011')