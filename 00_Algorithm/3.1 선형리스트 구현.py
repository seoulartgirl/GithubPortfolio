## 함수 선언부


## 전역 변수부
kakao = ['다현', '정연', '쯔위', '사나', '지효']

## 메인 코드부
print(kakao)

#! 데이터 추가 (모모에게 카톡 1회)
#1단계: 빈칸 추가
kakao.append(None)
#2단계: 데이터 넣기
kakao[5] = '모모'
print(kakao)

#! 데이터 삽입 (미나에게 연속 카톡 40회 -> 미나를 3등)
#1단계: 빈칸 추가
kakao.append(None)
#2단계: 한 칸씩 뒤로 이동
kakao[6] = kakao[5] #모모 이동
kakao[5] = None
kakao[5] = kakao[4] #지효 이동
kakao[4] = None
kakao[4] = kakao[3] #사나 이동
kakao[3] = None
#3단계: 새 친구 넣기
kakao[3] = '미나'
print(kakao)

#! 데이터 삭제 (사나(4등)가 카톡 차단)
#1단계: 데이터 지우기
kakao[4] = None
#2단계: 한 칸씩 앞으로 : 5등부터 마지막까지
kakao[4] = kakao[5] #지효 이동
kakao[5] = None
kakao[5] = kakao[6] #모모 이동
kakao[6] = None
#3단계 : 마지막 칸 제거
del(kakao[6])
print(kakao)

