#텍스트파일 읽기: read(), readline(), readlines(), seek()

#텍스트 파일 생성: 메모장을 이용해서
# 02_File_read_eng.txt : 한글
# 02_File_메모장.txt : 영문

#1단계: 파일열기(open)
# f = open('02_File_메모장', mode = 'r')
f = open('data/02_File_메모장', mode = 'r', encoding = 'utf-8')
text = f.read()
print(text)
f.close()

f1 = open('data/02_File_read_Eng', 'r') #r - read

#2단계: 파일처리(읽기)
#text = f1.read() #읽는것

text = f1.readline()
print(text) #결과: Hi! (첫줄)

text = f1.readline()
print(text) #결과: 띄어쓰기

text = f1.readline()
print(text) #결과: variable & constant

# readline()으로 파일읽기
# text = f.readline()
# print(text)
# text2 = f.readline()
# print(text2)

#readline() : 한줄씩 읽기
# while True:
#     text = f1.readline()
#     if not text: #텍스트가 비어있지 않으면 / 읽을 내용이 없으면 (마지막)
#         break
#     print(text)
    #결과: 한 행 출력하고 한줄 띄기

# readlines()로 파일읽기
#print(f1.readlines())
#결과: ['data type & operator\n', 'if statement\n', 'for statement\n', 'while']
#리스트 형태로 가져옴
# for textline in f.readlines():
#     print(textline, end='')

#readlines() 없이 파일읽기
for textline in f1:
    print(textline, end='') #end =''하면 줄띄움 없어짐
#결과:
# data type & operator
# if statement
# for statement
# while

#3단계: 파일닫기(close())
#f1.close()
f1.close()

# 영문으로 된 텍스트파일 읽기
# f1 = open('File_read_Eng.txt', mode='r')
# text = f1.read()
# print(text)
# f1.close()

#seek() : 내 탐색 위치 지정