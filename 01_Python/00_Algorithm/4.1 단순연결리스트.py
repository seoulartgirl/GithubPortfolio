##함수
#Node 데이터형 만들기 (붕어빵 틀 만들기)
class Node():
    def __init__(self):
        self.data = None
        self.link = None


##변수

##메인

node1 = Node()
node1.data = '다현'

node2 = Node()
node2.data = '정연'
#첫번째 노드에 두번째 노드 링크
node1.link = node2

node3 = Node()
node3.data = '쯔위'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5

newnode = Node()
newnode.data = '재남'
newnode.link = node2.link #node2.link = node3
node2.link = newnode

#노드 삭제 (쯔위)
# node2.link = node3.link
# del(node3)

# print(node1.data, end = ' ')
# print(node2.data, end = ' ')
# print(node3.data, end = ' ')
# print(node4.data, end = ' ')
# print(node5.data, end = ' ')

head = node1
# print(head.data, end =' ')
# print(head.link.data, end =' ')
# print(head.link.link.data, end =' ')
# print(head.link.link.link.data, end =' ')
# print(head.link.link.link.link.data, end =' ') # 다현 정연 쯔위 사나 지효
# print(head.link.link.link.link.link.data, end =' ') # 다현 정연 재남 쯔위 사나 지효
# 삭제 후 결과: 다현 정연 사나 지효

# print(node1.data, end = ' ')
# print(node1.link.data, end = ' ')
# print(node1.link.link.data, end = ' ')
# print(node1.link.link.link.data, end = ' ')
# print(node1.link.link.link.link.data, end = ' ')

##중요**
current = node1
print(current.data, end=' ') #이걸 안쓰면 첫번째 노드가 안나옴
while(current.link != None): #현재 노드가 비어있지 않고 링크되어있으면
    current = current.link #링크된 다음 노드로 변경
    print(current.data, end =' ') #마지막 노드까지 반복해서 출력
print()
