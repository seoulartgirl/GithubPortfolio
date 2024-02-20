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

#문제3.
str1 = 'this is'
str2 = 'PythON'
print(str1.title() + ' ' + str2.upper())

문제4:
sen = 'I like cooking!'

#결과: I like c$$king!

문제5:
#결과: 2022/01/01 -> 2032년 1월 1일

문제6: