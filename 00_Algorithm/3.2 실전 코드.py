## 함수
def add_data(friend):
    #1단계: 빈칸 추가
    kakao.append(None)
    kLen = len(kakao)
    #2단계: 추가한 빈칸에 친구 넣기
    kakao[kLen-1] = friend

def insert_data(position, friend):
    #1단계: 빈칸 추가
    kakao.append(None)
    #2단계: 한 칸씩 뒤로 이동(마지막 친구~ 바로 다음 친구까지)
    kLen = len(kakao)
    for i in range(kLen-1, position, -1):
        kakao[i] = kakao[i-1]
        kakao[i-1] = None #생략은 가능하나 두는걸 권장 / 깔끔하게 하기 위해
    #3단계: 포지션 자리에 친구 넣기
    kakao[position] = friend

def delete_data(position):
    #1단계: 위치 친구 지우기
    kakao[position] = None
    kLen = len(kakao)
    #2단계: 지운 친구 다음부터, 마지막 친구까지 앞으로 이동
    for i in range(position+1, kLen):
        kakao[i-1]=kakao[i]
        kakao[i] = None
    #3단계: 마지막 칸 제거
    # 안하면 이렇게 나옴 : ['다현', '정연', '쯔위', '미나', '지효', '모모', None]
    del(kakao[kLen-1])
    #결과: ['다현', '정연', '쯔위', '미나', '지효', '모모']

## 변수
kakao = []

## 메인
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(kakao) #결과: ['다현', '정연', '쯔위', '사나', '지효']
add_data('모모')
print(kakao) #결과: ['다현', '정연', '쯔위', '사나', '지효', '모모']

insert_data(3, '미나')
print(kakao) #결과: ['다현', '정연', '쯔위', '미나', '사나', '지효', '모모']


#데이터 삭제
delete_data(4) #사나 (4등) 카톡 차단
print(kakao) #결과: ['다현', '정연', '쯔위', '미나', '지효', '모모']


##선형 리스트의 일반 구현
## 함수 선언 부분
def add_data(friend):
    kakao.append(None)
    kLen = len(kakao)
    kakao[kLen-1] = friend

def insert_data(position, friend):
    #1단계: 빈칸 추가
    kakao.append(None)
    #2단계: 한 칸씩 뒤로 이동(마지막 친구~ 바로 다음 친구까지)
    kLen = len(kakao)
    for i in range(kLen-1, position, -1):
        kakao[i] = kakao[i-1]
        kakao[i-1] = None #생략은 가능하나 두는걸 권장 / 깔끔하게 하기 위해
    #3단계: 포지션 자리에 친구 넣기
    kakao[position] = friend

def delete_data(position):
    #1단계: 위치 친구 지우기
    kakao[position] = None
    kLen = len(kakao)
    #2단계: 지운 친구 다음부터, 마지막 친구까지 앞으로 이동
    for i in range(position+1, kLen):
        kakao[i-1]=kakao[i]
        kakao[i] = None
    #3단계: 마지막 칸 제거
    # 안하면 이렇게 나옴 : ['다현', '정연', '쯔위', '미나', '지효', '모모', None]
    del(kakao[kLen-1])
    #결과: ['다현', '정연', '쯔위', '미나', '지효', '모모']

## 변수
kakao = []
select = -1

#메인코드 부분
while (select !=4):

    select = int(input("선택하세요(1:추가, 2:삽입, 3:삭제, 4:종료)-->"))

    if (select == 1):
        data = input('추가할 데이터-->')
        add_data(data)
        print(kakao)
    elif (select == 2):
        pos = int(input("삽입할 위치-->"))
        data = input('추가할 데이터-->')
        insert_data(pos, data)
        print(kakao)
    elif (select == 3):
        pos = int(input("삭제할 위치-->"))
        delete_data(pos)
        print(kakao)
    else:
        print("1~4 중 하나를 입력하세요.")
        continue