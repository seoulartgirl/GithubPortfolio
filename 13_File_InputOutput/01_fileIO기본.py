#파일입출력을 위한 3단계

#1단계: 파일열기(open)
# 내장함수 open(파일경로, 모드)
# r,w,a,r+,w+,a+ : 텍스트 파일
# rb, wb, ab: 이진파일(binary 파일)
# 파일객체 = open(파일경로, 모드, 인코딩)

#2단계: 파일처리 => 읽기/쓰기
#파일객체.read()
#파일객체.write()

#읽기: 텍스트 파일 -> read(), readline(), readlines()
#쓰기: 텍스트 파일 -> write(), writelines()


#3단계: 파일 닫기(close())
#파일객체.close()


#위 3단계를 한번에 할 수 있는게 with문
# with문
# with open(파일경로, 모드, 인코딩) as 파일 객체:
#     파일읽기/쓰기

# 1) txt 파일 읽기/쓰기
# 2) csv 파일 읽기/쓰기 => csv 모듈
# 3) 이진파일 읽기/쓰기 : rb, wb
# 4) 객체 저장/읽기: dump & load -> pickle 모듈