'''
#다음 코드의 실행 결과를 쓰시오
#1-1
a = [0, 1, 2, 3, 4]
print(a[:3], a[:-3])
print(a[::-1])

#결과:[0,1,2] [0,1]
#[4,3,2,1,0] 거꾸로 실행


#1-2
first = ["egg", "salad", "bread", "soup", "canafe"]
second = ["fish", "lamb", "pork", "beef", "chicken"]
third = ["apple", "banana", "orange", "grape", "mango"]
order = [first, second, third]
john = [order[0][:-2], second[1::3], third[0]]
del john[2]
john.extend([order[2][0:1]])
print(john)

#결과: order = [["egg", "salad", "bread", "soup", "canafe"], ["fish", "lamb", "pork", "beef", "chicken"],["apple", "banana", "orange", "grape", "mango"]]
#john = [['egg', 'salad', 'bread'], ['lamb', 'beef'], 'apple']
#john = [['egg', 'salad', 'bread'], ['lamb', 'beef']] -> del 하면 'apple' 사라짐
#john.extend([order[2][0:1]]) -> [['egg', 'salad', 'bread'], ['lamb', 'beef'], ['apple']] -> order에 있는 ['apple'] 삽입


#1-3
list_a = [3, 2, 1, 4]
list_b = list_a.sort()
print(list_a, list_b)

#결과: [3,2,1,4] None
#풀이: list.sort()는 목록을 제자리에서 정렬하고 반환 값이 없어서 None

list_a = [3, 2, 1, 4]
list_b= sorted(list_a)
print(list_a, list_b)
#결과: [3, 2, 1, 4] [1, 2, 3, 4]


#1-4
a = [5, 7, 3]
b = [3, 9, 1]
c = a + b
c = c.sort()
print(c)

#결과: None
#풀이: list.sort()는 목록을 제자리에서 정렬하고 반환. 별도의 정렬 목록을 만들려면 직접 할당해야함.
a = [5, 7, 3]
b = [3, 9, 1]
c = a + b #[5,7,3,3,9,1]
c.sort() #[1,3,3,5,7,9]
print(c)


#1-5
num = [1, 2, 3, 4]
print(num * 2)

#결과: [1, 2, 3, 4, 1, 2, 3, 4]
#풀이: * 연산자를 통해 목록의 요소 반복할 수 있음
# 곱하기 2 하려면
num = [1, 2, 3, 4]
doub_num = [n*2 for n in num]
print(doub_num)
#결과: [2, 4, 6, 8]


#1-6
a = [1, 2, 3, 5]
b = ['a', 'b', 'c','d','e']
a.append('g')
b.append(6)
print('g' in b, len(b))

#결과: False 6
#풀이: a= [1,2,3,5,'g']
#b = ['a','b','c','d','e',6]


#1-7
country = ["Korea", "Japan", "China"]
capital = ["Seoul", "Tokyo", "Beijing"]
index = [1, 2, 3]
country.append(capital)
country[3][1] = index[1:]
print(country)

#결과: country = ["Korea", "Japan", "China", ["Seoul", [2,3], "Beijing"]]
#풀이: country = ["Korea", "Japan", "China", ["Seoul", "Tokyo", "Beijing"]]
#country[3][1] = "Tokyo" = [2,3]


#1-8
fruits = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry', 'melon']
print(fruits[-3:], fruits[1::3])

#결과: ['orange', 'strawberry', 'melon'] ['banana', 'orange'] 1부터 3칸씩


#1-9
list_a = ['Hankook', 'University', 'is', 'an', 'academic', 'institute', 'located', \
          'in', 'South Korea']
list_b=[ ]
for i in range(len(list_a)): #9
    if i % 2 != 1: #i % 2 == 0
        list_b.append(list_a[i]) #list_a의 짝수 인덱스에 요소를 추가
print(list_b)

#결과: ['Hankook', 'is', 'academic', 'located', 'South Korea'] 짝수 0, 2, 4, 6, 8


#2 다음 코드를 실행한 후, 2018과 "2018"을 각각 입력했을 경우
# 알맞은 실행 결과끼리 묶인 것은?

admission_year = input("입학 연도를 입력하세요: ")
print(type(admission_year))

#정답: 3번 - <class ‘str’>, <class ‘str’>


#3 다음 코드의 실행 결과가 나오도록 빈칸에 알맞은 코드를 쓰시오.
week1 = ["Mon", "Tue", "Wed"]
week2 = ["Thu", "Fri", "Sat", "Sun"]
week3 = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(week3[:len(week2) + 2])
#결과: week1 + week2
#결과:['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat’', sun]

#정답: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#풀이: week3[:4+2] / week3[:6]


#4-1 회원이름을 입력받아 회원명단 리스트를 생성 하고,
# 회원명단 리스트의 내용을 출력하는 코드를 완성하시오.
#회원입력: 홍길동 / 회원입력: 이몽룡 / 회원입력: 성춘향 / 회원명단: 홍길동, 이몽룡, 성춘향

name_list = []
for i in range(3):
    name = input(f'회원{i+1} 이름 입력:')
    name_list.append(name)
    #name_list(append(input(f'회원{i+1} 이름 입력:'))) -> 이렇게 해도 됨
print(name_list)


#4-2 학생 수를 입력받아 학생의 수만큼 점수를 입력받은 후 총점과 평균을 계산하고,
# 80점 이상인 학생의 수를 출력하는 코드를 작성하시오.
# 학생의 점수는 리스트로 생성한다.
#결과
#학생 수 입력: 3 / 학생1 점수 입력: 91 / 학생2 점수 입력: 78 / 학생3 점수 입력: 85
#총점: 254 / 평균: 84.67 / 80점 이상 학생: 2명

sn = int(input('학생 수 입력:'))
score_list = []
cnt=0
for i in range(sn):
    score = int(input(f'학생{i+1} 점수 입력:'))
    score_list.append(score)
    total = sum(score_list)
    avg = total / sn
    if score > 80:
        cnt += 1
print(f'총점:{total}')
print(f'평균:{avg:.2f}')
print(f'총점:{cnt}명')
#---------------------- 4-4번
print(sorted(score_list, reverse=True))


#4-3 상품을 리스트에 추가하고 엔터키를 누르면 입력이 종료되고
# 등록된 상품 리스트를 출력하는 코드를 작성하시오.
#결과: 상품 등록(엔터키 누르면 종료) : 노트북.. 마우스.. 키보드
#등록된 상품: 노트북 마우스 키보드

#code1
i=0
pr_list = []
while True:
    entry = input(f'상품{i+1} 등록(엔터키 누르면 종료):')
    pr_list.append(entry)
    i += 1
    if not entry: #if item == '' 엔터키 누르면
        break
print(f'등록된 상품:{pr_list}')

#결과: 등록된 상품:['notebook', 'mouse', 'keyboard', ''] -> 마지막 ''빼는법?

#code2
totentry=''
i =0
while True:
    entry = input(f'상품{i+1} 등록(엔터키 누르면 종료):')
    totentry += entry + ' '
    i += 1
    if not entry:
        break
print(f'등록된 상품: {totentry}')

'''

#4-4 4-2 문제에서 학생들의 점수를 내림차순으로 정렬하여 출력하는 코드를 추가하여 작성하시오.
#결과: 점수 내림차순 정렬 : [91,82,78,77,69]

#정답: 4-2 참고

#4-5 사자성어 맞추기 게임을 작성하시오. [조건]
#사자성어와 관련 뜻은 리스트 2개로 작성한다.
#사자성어를 맞출때까지 계속 한다.

words=["개과천선", "구사일생", "군계일학", "무용지물", "동고동락", "유비무환", "입신양명",\
        "괄목상대", "막역지우", "고장난명"]
sents= ["잘못을 고치고 옳은 길에 들어섬", "죽일 고비를 여러 번 겪으며 살아나다",\
       "평범한 사람 가운데 뛰어난 사람", "아무짝에나 쓸모 없는 것",\
       "고통과 즐거움을 함께 한다", "미리 준비해두면 근심 걱정이 없다",\
        "사회적으로 인정받고 출세하여 이름을 세상에 드날림", "다른 사람의 학식이나 업적이 크게 진보한 것을 말함",\
        "생사를 같이 할 수 있는 친밀한 벗", "상대 없이 혼자서는 어떤 일을 이룰 수 없다"]

#리스트 두개 끼리끼리 묶는법
print(list(zip(words, sents))) #리스트
print(dict(zip(words, sents))) #딕셔너리
print({'사자성어': words, '뜻': sents}) #딕셔너리

print('사자성어 맞추기 게임을 시작합니다')
print('-------------------------')
import random

sent = random.randint(0, len(sents)-1)
random_sent = sents[sent]
i=0
while True:
    answer = input(f'문제{i+1}: {random_sent}. 이 말의 사자성어는?:')
    if answer in words:
        if words.index(answer) == sents.index(random_sent):
            print('맞습니다.. 게임을 종료합니다')
            break
    else:
        print('틀렸습니다.. 다시 도전 !')
        i = i+1

#break 전에 print 해야함
