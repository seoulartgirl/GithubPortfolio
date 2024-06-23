#리스트 컴프리헨션
#기본 형식:
#새로운 리스트= [반복문장 for 변수 in 반복범위(예.range()) [if 조건식]]

num_list = []
for num in range(1,6):
    num_list.append(num)
print(num_list)
#결과: [1, 2, 3, 4, 5]

num_list = [num for num in range(1,6)]
print(num_list)
#결과: [1, 2, 3, 4, 5]

num_list = [num*2 for num in range(1,6)]
print(num_list)
#결과: [2, 4, 6, 8, 10] 곱하기 2한 문장

num_list = [num**2 for num in range(1,6)]
print(num_list)
#결과: [1, 4, 9, 16, 25] 제곱한 문장


#1) 문제1: 1~20의 정수 중 짝수만으로 구성된 리스트 생성
#code1
list= [num for num in range (2,21,2)]
print(list)
#결과: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#code2
list= [num for num in range (1,21) if num %2 ==0]
print(list)
#결과: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#code3
num_list = []
for num in range(1,21):
    if num % 2 == 0:
        num_list.append(num)
print(num_list)

#2) 문제2: 1~20의 정수 중 3의 배수로만 구성된 리스트 생성
num_list = [num for num in range(3,21,3)]
print(num_list)
#결과: [3, 6, 9, 12, 15, 18]

num_list = [num for num in range(1,21) if num%3==0]
print(num_list)
#결과: [3, 6, 9, 12, 15, 18]


#참고. zip 함수

foods = ['떡볶이', '짜장면', '라면', '피자']
sides = ['단무지', '김치', '피클']

for food, side in zip(foods, sides):
    #zip 함수 같은 인덱스에 있는 것들을 묶어버림
    print(food, '--', side)

#결과:
# 떡볶이 -- 단무지
# 짜장면 -- 김치
# 라면 -- 피클

for food, side in zip(sides, foods, strict=False): #stirct-True
    print(food, '--', side)

#결과:
# 단무지 -- 떡볶이
# 김치 -- 짜장면
# 피클 -- 라면

for item in zip(foods, sides):
    print(item)
    print(type(zip(foods, sides)), zip(foods, sides))
#결과:
# ('떡볶이', '단무지') <class 'zip'> <zip object at 0x104b47440>
# ('짜장면', '김치') <class 'zip'> <zip object at 0x104b47440>
# ('라면', '피클') <class 'zip'> <zip object at 0x104b47440>



name = ['홍길동', '강감찬', '성춘향', '방자']
sex = ['남', '남', '여', '남']
addr = ['서울', '한양', '독도', '부산']

# print(list(zip(name, sex, addr)))
#TypeError: 'list' object is not callable 위에 리스트를 변수로 사용해서 발생 에러

#결과: [('홍길동', '남', '서울'), ('강감찬', '남', '한양'), ('성춘향', '여', '독도'), ('방자', '남', '부산')]
