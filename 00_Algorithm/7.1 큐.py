## 함수


## 변수
#큐의 초기화----------------------------
SIZE= 5
queue = [None for _ in range(SIZE)]
front=rear= -1
#큐의 초기화----------------------------

## 메인
#! enQueue()
rear += 1
queue[rear] = '화사'
print('출구<--', queue, '<--입구')

rear += 1
queue[rear] = '솔라'
print('출구<--', queue, '<--입구')

rear += 1
queue[rear] = '문별'
print('출구<--', queue, '<--입구')

#! deQueue()
front += 1
data = queue[front]
queue[front] = None
print('식사 손님:', data)

front += 1
data = queue[front]
queue[front] = None
print('식사 손님:', data)

front += 1
data = queue[front]
queue[front] = None
print('식사 손님:', data)

print('출구<--', queue, '<--입구')