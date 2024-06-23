#문제1-1
fact = 'Python is funny'
print(str(fact.count('n') + fact.find('n') + fact.rfind('n')))

#정답: 21
#풀이: 3 + 5 + 13 = 21

#문제1-2
text1 = 'Python is a programming language'
text2 = 'and integrate systems more effectively'

text1.lower()
print(text1[:7] + text2.split()[-1] + text1[-9:])

#정답: Python effectively language
#풀이:
# text1[:7] : 'Python '
# text2.split()[-1] : 'and' 'integrate' 'systems' 'more' 'effectively' 중 마지막
# text1[-9:]) : ' language' 뒤에서부터 9번째 부터 끝까지

#문제1-3
text = 'Python is a programming language'
temp =''
for i in text.split():
    print(i)
    if i == 'language':
        temp = i.upper() + ' ' + temp
    else:
        temp = i + ' ' + temp
print(temp)

#정답: LANGUAGE programming a is Python
#풀이: Python is a programming LANGUAGE
# # -> temp가 뒤에 있어서 반대로 출력

#문제1-4
text = '문자열을 입력하세요'
print('{1},{0}'.format(text[-3], text[:4]))

#정답: 문자열을, 하
#풀이:
# text[-3] : 하
#text[:4] :문자열을

#문제2.
print('{0:>10s}'.format('python'))

#정답:     python
#10자리에서 오른쪽으로 출력 됨

#문제3.
str1 = 'this is'
str2 = 'PythON'
print(str1.title() + ' ' + str2.upper())

#정답: This Is PYTHON
#풀이: 제목화, 대문자화

#문제4:
#code1 - replace 함수 사용
sen = 'I like cooking!'
sen = sen.replace('o', '$')
print(sen)

#code2 -replace 함수 사용 X
sen = input('문자열을 입력하세요:')
temp =''
for ch in sen:
    if ch == 'o':
        temp += '$'
    else:
        temp += ch
print(temp)

#결과: I like c$$king!

#문제5: 날짜 10년 뒤로 출력
#결과: 2022/01/01 -> 2032년 1월 1일
from datetime import date, timedelta

targetdate = date(2022, 1, 1)
tenyears = targetdate + timedelta(days=365*10)
print(tenyears)
#2031-12-30

#문제6: 숫자 입력하는 만큼 하트 출력하기
heart = '\u2665'
nums = input('숫자를 여러개 입력하세요:')
for i in nums:
    print(heart*int(i))

#결과: 123 입력시
# ♥
# ♥♥
# ♥♥♥
