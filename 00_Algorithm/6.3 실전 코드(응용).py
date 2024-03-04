# 스택 응용
# 1. 함수 호출
# a() -> b() -> c() -> d()
# a에서 b를 호출 (push, push)
# 2. 괄호 오류 검사
# ((()()()))()
# -> 여는 괄호 push, 닫는괄호 pop 설정

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

def checkBracket(ex):
    for ch in ex:
        if ch == '(':
            push(ch)
        elif ch ==')':
            data = pop()
            if (data == '('):
                pass
            else:
                return False
    if top == -1 : #스택이 깔끔하게 비었니?
        return True
    else:
        return False


## 변수
SIZE = 50 #전역상수. 대문자 표기 (숫자라는걸 명시)
stack = [None for _ in range(SIZE)]
top = -1

## 메인
expr = '(())()()(())'
retTF = checkBracket(expr)

#print(expr)
if (retTF): #True면
    print('정상')
else:       #False면
    print('오류')

## 미니특강2 : 현업 알고리즘 테스트 문제
## 배경 : 구글 >> 삼성, LG, SK ...
## - A기업: 1문제(5시간) ==> 극상
## - B기업: 4문제(4시간) ==> 상, 중, 하, 하하

