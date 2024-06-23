#재귀
## 함수

# def openBox():
#     print('상자열기~~')
#     openBox()

## 메인
# openBox() #무한루프 돔


##함수
def openBox():
    global count
    print('상자열기~~')
    count -= 1
    if count == 0:
        print('***선물 넣기***')
        return
    openBox()
    print('상자닫기###')

## 메인
count = 10
openBox()
