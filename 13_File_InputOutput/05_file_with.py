#with문: close()가 자동을 수행
#qith open(파일명, 모드) as 파일객체:
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

