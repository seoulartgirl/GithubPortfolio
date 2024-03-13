#with문: close()가 자동을 수행
#with open(파일명, 모드) as 파일객체:
#       수행문장들

# with open('data/02_File_read_Eng', 'r') as f:
#     text = f.read()
#     print(text)
#
# with open('data/05_file1.txt', 'a') as f:
#     f.write(text)

#with문은 close 쓸 필요없음

#scores.txt: 탭으로 구분한 데이터 파일
with open('data/05_scores.txt', 'r') as f:
    data = f.readlines()
    print(data)

#결과: ['이름  성별  나이  국어  영어  수학\n', '홍길동 남   15  90  90  80\n', '성춘향 여   16  80  90  100']

#scores2.txt : ,으로 구분한 데이터 파일
with open('data/05_scores2.txt', 'r') as f:
    data = f.readlines()
    print(data)

#결과: ['이름,성별,나이,국어,영어,수학\n', '홍길동,남,15,90,90,80\n', '성춘향,여,16,80,90,100']

print(len(data)) #결과: 3

#리스트로 추출 방법
score=[]
for i in range(len(data)):
    temp=data[i]
    temp=temp.rstrip('\n')
    score=score+temp.split(',')

print('score',score)
#결과: score ['이름', '성별', '나이', '국어', '영어', '수학', '홍길동', '남', '15', '90', '90', '80', '성춘향', '여', '16', '80', '90', '100']
