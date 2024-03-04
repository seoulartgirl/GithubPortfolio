#문제1.
#학생들의 이름과 성적을 딕셔너리로 저장하고 있다.
#이 딕셔너리를 사용하여 각 학생 의 성적에 대한 총점과 평균을 계산하여 출력하는 코드를 작성하시오.

#딕셔너리로 이루어진 리스트
students = [{"name": '홍길동',"korean": 87, "math": 98, "english": 88, "science": 95},
            {"name": "이몽룡","korean": 92, "math": 98, "english": 96, "science": 98},
            {"name": "성춘향", "korean": 76, "math": 96, "english": 94, "science": 90},
            {"name": "변학도", "korean": 98, "math": 92, "english": 96, "science": 92},
            {"name": "박지성", "korean": 95, "math": 98, "english": 98, "science": 98},
            {"name":"류현진", "korean": 64, "math": 88, "english": 92, "science": 92}]

print('이름', '총점', '평균')
#print('{0:6s}{1:6s}{2}'.format('이름', '총점', '평균'))
for s in students:
    name = s['name']
    tot = s["korean"] + s["math"] + s["english"] + s["science"]
    avg = tot / 4
    print(name, tot, avg)

#문제2: 딕셔너리를 이용하여 사용자로부터 영어단어와 뜻을 입력받아 사전을 구성하고,
# 사용자가 입력한 단어를 검색하여 뜻을 출력하는 프로그램을 작성하시오.

word_dic={}
while True:
    engword = input('영어 단어 등록(종료는 quit):')
    if engword == 'quit':
        #print('종료합니다.')
        break
    elif engword in word_dic:
        print(f'{endword}는 이미 등록된 단어입니다.')
    else:
        meaning = input(f'{engword}의 뜻 입력(종료는 quit):')
        if meaning == 'quit':
            #print('종료합니다.')
            break
        word_dic[engword] = meaning

while True: #무한루프
    search = input('검색할 단어 입력(종료는 quit):')
    if search == 'quit':
        print('종료합니다.')
        break
    if search in word_dic:
        print(f'{search}의 뜻은 {word_dic[search]}입니다.')
    else:
        print(f'{search}는 사전에 없는 단어입니다.')

#문제 3: 다음 중 오류가 발생하는 경우는 고르고, 그 원인을 설명하시오.

# a['name'] = 'python' #딕셔너리의 키로 문자열이 옴
# a[('a',)] = 'python' #튜플이 옴
# a[[1]] = 'python' #리스트는 오류 발생
#TypeError: 딕셔너리의 키로는 변경가능한 자료 사용 불가
# a[250] = 'python' #숫자 가능


#문제4: 다음 코드에서 오류가 발생한다. 그 원인을 설명하시오.
# t = (1, 2, 3)
# t[0] = 'a'
#튜플은 변경 불가, 인덱스 0에 변수 할당 불가능 -> 리스트면 가능

t = [1, 2, 3]
t[0] = 'a'

#문제5: 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
#t = 1, 2, 3, 4
#정답: 튜플에 있는 int(정수형)

#문제6:
#1)
my_variable = ()
print(type(my_variable))

#2)
tup = (1,) #t=1,
print(type(tup))

#3)
t = ('a','b','c') #t=tuple('abc')문자 단위로 쪼개져서 들어감
print(type(t))

#4)
#방법1
del t
t = ('A','b','c')
print(t)

#방법2
t2 = list(t)
t2[0] = 'A'
t=tuple(t2)
print(t)

#5)다음 튜플을 리스트로 변경
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest2 = list(interest)
print(interest2)

#6) 다음 리스트를 튜플로 변경
interest = ['삼성전자', 'LG전자', 'SK Hynix']
print(tuple(interest))

#7) (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만든 후 출력
#방법1
tup1 = (1,2,3)
list2=list(tup1)
list2.append(4)
tup1=tuple(list2)
print(tup1)

#방법2
tup1=1,2,3
print(tup1)
tup2 = tup1 + (4,)
print(tup2)

#8) 다음 딕셔너리에서 ’B’에 해당하는 값 추출하고 삭제
a = {'A':90, 'B':80, 'C':70}
print(a['B']) #80
a.pop('B')
print(a)
# a.pop() 오류남 - 키 값 안쓰면


#7. 파티에 참석한 사람이 다음과 같을 때 세트를 생성하고, 아래 조건에 맞게 출력하는 코드를 작성하시오.
partyA = {"Park","Kim","Lee"}
partyB = {"Park","길동","몽룡"}
#1) 파티에 참석한 모든 사람은?
print(partyA | partyB)

#2) 2개의 파티에 모두 참석한 사람은?
print(partyA & partyB)

#3) 파티 A에만 참석한 사람
print(partyA-partyB)

#4) 파티 B에만 참석한 사람
print(partyB-partyA)