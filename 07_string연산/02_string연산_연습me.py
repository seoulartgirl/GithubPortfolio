#1. 문자열의 모든 글자 뒤에 $ 붙이기
#1단계
s = '파이썬짱!'
for ch in s:
    print(ch+'$')

#2단계
s = '파이썬짱!'
temp=''
for ch in s:
    temp = temp + ch + '$'
print(temp)

#문자의 짝수번째 글자는 모두 #으로 변경하여 출력하기

text = '파이썬은재미있어요'
for ch1 in text:
    print(ch1)

print('code 1 ---------------------')

text = '파이썬은재미있어요'
for ch1 in text[::2]:
    print(ch1, end = '#')


print('code 2---------------------')


text = '파이썬은재미있어요'
#code1
temp2 =''
for ch1 in text[::2]:
    temp2 = temp2 + ch1 + '#'
print(temp2)

# 결과: 파#썬#재#있#요

print('code 3---------------------')

temp = ''
for ch in text:
    if ch%2==0:
        ch = '#'
    else:
        pass
    temp += ch
print(temp)

print('code4---------------------')

temp =''
for text in range(len(s)):
   ch = '#' if text % 2 != 0 else s[text]
   temp += ch
print(temp)

