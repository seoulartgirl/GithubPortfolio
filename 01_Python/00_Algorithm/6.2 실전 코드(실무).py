## 함수
def isStackFull() : #스택이 꽉 찼느냐 묻는 함수
    global SIZE, stack, top
    if (top >= SIZE-1): # '==' 같다 해도 됨
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if (isStackFull()): #True면
        print('Stack Overflow!')
        return
    top += 1
    stack[top] = data

def isStackEmpty():
    global SIZE, stack, top
    if (top <= -1): # '==' 같다 해도 됨
        return True
    else:
        return False

def pop():
    global SIZE, stack, top
    if (isStackEmpty()) : #True문
        print('Stack Underflow!')
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global SIZE, stack, top
    if (isStackEmpty()):
        print('Stack Underflow!')
        return
    return stack[top]

## 변수
SIZE = 5 #전역상수. 대문자 표기 (숫자라는걸 명시)
stack = [None for _ in range(SIZE)]
top = -1

## 메인

push('커피')
push('녹차')
push('꿀물')
push('콜라')
push('환타')
push('제로')              #Stack Overflow!
print('바닥:', stack)      #바닥: ['커피', '녹차', '꿀물', '콜라', '환타']

retData = pop()
print('팝 데이터-->', retData)      #팝 데이터--> 환타
print('바닥:', stack)     #바닥: ['커피', '녹차', '꿀물', '콜라', None]

retData = pop()
print('팝 데이터-->', retData)      #팝 데이터--> 콜라
print('바닥:', stack)     #바닥: ['커피', '녹차', '꿀물', None, None]

retData = pop()
print('팝 데이터-->', retData)      #팝 데이터--> 꿀물
print('바닥:', stack)     #바닥: ['커피', '녹차', None, None, None]

print('다음 예정:', peek()) #다음 예정: 녹차


##함수 선언 부분##
def isStackFull():
    global SIZE, stack, top
    if (top >= SIZE-1):
        return True
    else:
        return Flase

def isStackEmpty():
    global SIZE, stack, top
    if (top == -1):
        return True
    else:
        return False
