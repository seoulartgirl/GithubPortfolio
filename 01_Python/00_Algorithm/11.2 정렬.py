## 함수
from random import randint
def findMinIndex(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if ary[minIdx] > ary[i]:
            minIdx = i
    return minIdx

## 변수
before = [randint(30,190) for _ in range(8)]
after = []

## 메인
print('정렬 전 -->', before)
for _ in range(len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del before[minPos]
    # del 안쓰면 [43, 43, 43, 43, 43, 43, 43, 43] 이렇게 작은게 계속 반복됨

print('정렬 후 -->', after)
