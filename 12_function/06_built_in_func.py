#내장함수들

#abs(): 절대값
print(abs(-10)) #결과: 10

#all(iterable) : 모두 True인 경우 True
#any(iterable) : 하나라도 True인 경우 True
print(all([0,1,2,3])) #False - 0이 있으면 false
print(any([1,0,'',[]])) #True

#chr(), ord() : 아스키 코드값
print(chr(65)) #결과: A
print(ord('A')) #결과: 65

#divmod(), pow()
#min(), max(), sum()
print(max([1,2,3,4,-10])) #결과: 4
print(min([1,2,3,4,-10])) #결과: -10
print(sum([1,2,3,4,-10])) #결과: 0

#round(number, ndigits) : 반올림
print(round(3.141592712345)) #결과: 3
print(round(3.141592712345, 2)) #결과: 3.14

#enumerate() : 인덱스 값을 포함한 enumerate 객체 반환
print(list(enumerate(['kim', 'lee','choi'])))
#결과: [(0, 'kim'), (1, 'lee'), (2, 'choi')]

data = ['kim', 'lee','choi']
for item in enumerate(data):
    print(item)
# 결과 :
# (0, 'kim')
# (1, 'lee')
# (2, 'choi')

for idx, value in enumerate(data):
    print(idx, value)
# 결과:
# 0 kim
# 1 lee
# 2 choi

for idx, value in enumerate('Hello World!'):
    print(idx,value)
#결과:
# 0 H
# 1 e
# 2 l
# 3 l
# 4 o
# 5
# 6 W
# 7 o
# 8 r
# 9 l
# 10 d
# 11 !

#eval(표현식): 표현식을 그대로 실행

print(eval('10')) #결과: 10
print(eval('10*10')) #결과: 100
print(eval('10'+'10')) #결과: 1010

#filter(): 반복가능한 자료에 어떤 함수를 적용하여 True인 결과만 추출
def positive(x):
    return x>0

def even(x):
    if x % 2 == 0:
        return x

print(positive(10)) #True
print(positive(-10)) #False

print(list(map(positive, [1,2,-1,10, -5])))
#결과: [True, True, False, True, False]
print(list(filter(positive, [1,2,-1,10, -5])))
#결과: [1, 2, 10] / 해당되는 결과만 뽑아옴

def even(x):
    if x % 2 == 0:
        return x
x = 4
print(even(x)) #결과: 4

print(list(filter(even, [1,2,-1,10, -5])))
#결과: [2, 10]

#help() : 도움말 시스템 호출
help(print)
help(filter)
help(sum)

#int(), float(), str()
#bin(), hex(), oct()
#input(), print()
#zip(), map()
#range()
#len()
#list(), tuple(), dict(), set()
#id(), type()
#lambda()