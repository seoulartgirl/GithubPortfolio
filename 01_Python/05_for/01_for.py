#반복문 for
#1. 문제1: 1~10 사이의 정수를 더하기
'''
#code1 - 원시적 방식
total = 1+2+3+4+5+6+7+8+9+10
print(total)

#code2
total = 0
total = total + 1
total = total + 2
total = total + 3
total = total + 4
total = total + 5
total = total + 6
total = total + 7
total = total + 8
total = total + 9
total = total + 10
print(total)

#code3 아래와 같이 간소화
total = 0
for num in range(1,11):
    total = total + num
print(total)


#2. 문제2: 1부터 10사이의 홀수를 더하기
total = 0
for num in range(1,11,2):
    total = total + num
print(total)


#3. 문제3: 1부터 10사이의 짝수를 더하기
total = 0
for num in range(0,11,2):
    total = total + num
print(total)


#4. 문제4: 시작값, 끝값을 입력 받아 시작값~끝값까지 정수더하기
start = int(input('시작값:'))
end = int(input('끝값:'))
total=0 #total 0으로 꼭 잡아주기
for num in range(start, end+1):
    total += num
print(total)


#5. 문제5: 구구단 출력
x=0
y=0
for x in range(1, 10):
    for y in range (1, 10):
        print(f'{x}X{y}={x*y}')

'''
#다중 for을 이용
for x in range(3):
    print(x)
    for y in range(1, 5):
        print(y+4*x, end=' ')
    print()

#결과 값:
#0
#1 2 3 4
#1
#5 6 7 8
#2
#9 10 11 12


a = 0
for x in range(3):
    for y in range(4):
        a += 1
        print(a, end=' ')
    print()

#결과 값:
#1 2 3 4
#5 6 7 8
#9 10 11 12

#6. 문제6: 5명의 점수 입력받아 합격>=60, 불합격<60 출력

for num in range(5):
    score=int(input('점수 입력:'))
    if 0 > score or score > 100:
        print('0~100사이 입력해주세요')
    elif score >= 60:
        print('합격')
    else: print('불합격')
