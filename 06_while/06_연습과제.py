#1.
a=123
if a > 100:
    if a > 200:
        print('완전히 큰 수 입니다.')
    else:
        print('적당한 수 입니다.')
else :
    print('완전히 작은 수 입니다.')
    print('프로그램 끝입니다.')

#정답: 적당한 수입니다.

#2.
num = ['12', '34', '56']
for i in num: # in뒤의 요소들을 i에 대입
    i = int(i)
print(num) #원래 있는 i 그대로 나옴 페이크임
print(i) #결과: 최종적인 숫자 56이 나옴

num = ['12', '34', '56']
res = ''
for i in num:
    res += i
print(res)
#결과: ['12', '34', '56']

#정답: ['12', '34', '56'] / int 정수로 변환했는데 str으로 출력되는 이유?
#페이크 임 [12, 34, 56] 아닌, ['12', '34', '56']

#3.
cnt = 0
for i in range(1, 100, 4):
    print('파이썬 꿀잼')
    cnt += 1
print(f'{cnt}회 출력')

#정답: 25번 / (99//4=24 -> 24개 이고 1까지 총 25개)

#4.
num = 0
i = 1
while i<8:
    if i % 3 ==0:
        break
    i +=1
    num += i
print(num)
#정답; 5  / (3의 배수 되기 전까지 통과 i = 2, num =2 / i =3, num =5 / i=3 에서 break)


#5.
result = 0
for i in range(5, -5, -2):
    if i < -3:
        result += 1
    else:
        result -= 1

print(result)

#정답 : -5 / range(5,3,1,-1,-3) 전부다 -3보다 크거나 같음 -> else로 가서 -5

#6.
fruit = 'apple'
if fruit == 'Apple':
    fruit == 'Apple'
elif fruit == 'fruit':
     fruit == 'fruit'
else:
    fruit = fruit
print(fruit)

#정답: 'apple' / if, elif 조건이 둘다 거짓 -> else인데 /리터럴에 선언된적 없는 변수가 들어감

#7.
first_value=0
second_value=0
for i in range (1,10):
    if i == 5:
        continue
        first_value=i
    if i == 10:
        break
        second_value=i
print(first_value+second_value)

#정답: 0 / 만약 range(11) 이면 0 + 10 이 됨

#8.
num = "" #''빈문자열
for i in range(10):
    if i <=5 and (i % 2) == 0:
        continue
    elif i == 7 or i == 10:
        continue
    else:
        num = str(i) + num # 1 + ''(빈 문자열) 하나의 문자열로 합쳐줌
        # 만약 num = num + str(i) 하면 결과 135689 나옴
print(num)

#정답: 986531

#9.
coupon = 0
money = 200000
coffee = 3500
cnt = 0
c_cnt = 0
while money > coffee:
    if coupon < 4:
        money = money - coffee
        coupon += 1
    else:
        money += 2800
        coupon = 0
        c_cnt += 1
    cnt += 1

print(money, cnt, c_cnt)

# 정답: 2600 87 17

#10.
list_data_a=[1,2]
list_data_b=[3,4]

result1 = 0
for i in list_data_a:
    for j in list_data_b:
        result2 = i + j
        result1 += i + j
print('최종 변수:', result2, '총 합계:', result1)

#정답: 6

#11-1. 역삼각형 출력
star = '*'
for i in range(5,0,-1):
    print(star*i)

#11-2. 피라미드 출력
#code1 - for문
star = '*'
space = " "
for i1 in range(1,10,2):
    space=''*((9-i1)//2)
    print(space, "*"*i1)

