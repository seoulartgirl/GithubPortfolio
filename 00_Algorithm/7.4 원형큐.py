## 함수
def isQueueFull():
    global SIZE, queue, front, rear
    #원형큐
    if (rear+1) % SIZE == front: #꼬리 +1 이 머리면 꽉참
        return True
    else: return False

def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print('큐 꽉!')
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data

def isQueueEmpty() :
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False

def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('큐 텅!')
        return
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('큐 텅!')
        return
    return queue[(front+1)%SIZE]

#한칸 비워둔게 꽉찬 상태, 원형 큐 가장 깔끔한 형태, 오버헤드 발생X

## 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = 0

## 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print('출구<--', queue, '<--입구')

enQueue('수정')
print('출구<--', queue, '<--입구')

#데이터 추출
retData = deQueue()
print('손님 이리로 : ', retData)

# retData = deQueue()
# print('손님 이리로 : ', retData)

# retData = deQueue()
# print('손님 이리로 : ', retData)

peekData = peek()
print(peekData)