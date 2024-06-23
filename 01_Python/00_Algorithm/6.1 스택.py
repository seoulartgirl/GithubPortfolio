## 함수
## 변수

stack = [None, None, None, None, None]
top = -1 #비어있는 상태 지하 -1층인 상태 / 0 하면 빈 상태X


## 메인
# Push() : 데이터 삽입
top += 1
stack[top] = '커피'
top += 1
stack[top] = '녹차'
top += 1
stack[top] = '꿀물'
print('바닥:', stack) #바닥: ['커피', '녹차', '꿀물', None, None]


# Pop() : 데이터 추출
data = stack[top]
stack[top] = None
top -= 1
print('pop:', data) #pop: 꿀물
print('stack:', stack)
#stack: ['커피', '녹차', None, None, None]

data = stack[top]
stack[top] = None
top -= 1
print('pop:', data) #pop: 녹차
print('stack:', stack)
#stack: ['커피', None, None, None, None]

data = stack[top]
stack[top] = None
top -= 1
print('pop:', data) #pop: 커피
print('stack:', stack)
#stack: [None, None, None, None, None]
