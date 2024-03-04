#1. 리스트 요소 추가: append(), insert()

#1) 문제1: 3명의 회원을 입력받아 리스트에 추가하기
# 회원 입력: 홍길동
# 회원 입력: 이몽룡
# 회원 입력: 성춘향
# 회원 명단: ---

#code1 - 원시적 방법
# name1 = input('회원 입력:')
# name2 = input('회원 입력:')
# name3 = input('회원 입력:')
# name = []
# name.append(name1)
# name.append(name2)
# name.append(name3)
# print(name)

#code2
name_list = []
for i in range(3):
    name = input(f'회원{i+1} 입력:')
    name_list.append(name)
print(name_list)

#code3
name_list = []
#i = 0
while True:
    name = input(f'회원 입력:')
    if name == 'x':
        break
    else:
        name_list.append(name)
print(name_list)


# 회원 명단 출력 - 홍길동, 이몽룡, 성춘향 / hong, lee, sung
print(name_list) #hong, lee, sung
for name in name_list:
    print(name)
    #결과:
    #hong
    #lee
    #sung

#2) 문제2: 5명 점수 입력받아 리스트 추가, 총점, 평균 계산 후 출력

#code1
total=0
score_list =[]
for i in range(5):
    score= int(input(f'점수{i+1}입력:'))
    score_list.append(score)
    total += score
    avg = total/len(score_list)

score_list.append(total)
score_list.append(avg)
print(score_list)

#code2
total = 0
scores = []
for i in range(5):
    score= int(input(f'점수{i+1}입력:'))
    scores.append(score)
for score in scores:
    total += score
avg = total / len(scores)
print(f'총점: {total}')
print(f'평균: {avg:.2f}')

#3. 문제3: 80점 이상의 학생 수를 계산 (78, 91, 64, 77, 83)
#학생1 점수 입력: ~ 학생5: / 80점 이상 학생: 2명

#위 코드에 +
cnt = 0
for score in scores:
    if score >= 80:
       cnt += 1

print(f'80점 이상 학생: {cnt}명')

#4. 문제4: 엔터키를 누를 때 까지 상품명들을 리스트에 추가하고
#엔터키를 누르면 입력 종료되고 등록된 함수 출력

