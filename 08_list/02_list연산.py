#1. 인덱싱(indexing) : 요소 접근

a = [1,2,3,4,5]
b = [[1,2],3,[5,6]]
print(a[0], a[-1], a[3])
print(b[0], b[2], b[0][0])

#2. 슬라이싱(slicing) : 부분 문자열
print(a[:]) #전체
print(a[1:])
print(a[:2])
print(a[::2])
print(a[::-1])

#3. 리스트 값 변경: 인덱스를 이용 a[i] = 값
#인덱스를 이용 a[i]=값
print('변경전 리스트',a) #변경전 리스트
a[1] = 100
print('변경후 리스트', a) #변경후 리스트

print(a)
a[2] = [10,20]
print('변경후 리스트',a)

#슬라이싱을 이용 -> 여러개 자를 수 있음

a[1:2]= [30,40]
print('변경 후 리스트', a)

c = [10,20,30]
x,y,z = c
print(x,y,z)

# 4. 리스트 합치기: +
a = [1,2,3,4]
b=[7,8,9,10]
print(a+b)

#5.리스트 곱하기 (반복) *
print(a*3) #리스트가 세번 반복됨

#인덱싱, 슬라이싱, +, *, 멤버 in not in

#6. 리스트 복사(copy) : 깊은 복사 vs 얕은 복사
a = 10
b = a
b = 15
print(a, b)

a_list = [10,20,30,40]
b_list = a_list
#shallow copy (얕은 복사) -> 한쪽이 바뀌면 다른쪽도 바뀜
#리스트는 복사되지 않고 주소값만 복사

a_list[0] = 'apple'
print(a_list, b_list)
b_list[-1]='banana'
print(a_list, b_list)
#리스트에서는 b도 같이 바뀜

a_list = [10,20,30,40]
c_list = list(a_list) #deep copy(깊은 복사)
#리스트의 복사본을 새로 생성하여 반환
a_list[0] = 'apple'
print(a_list, b_list)
c_list[-1]='banana'
print(a_list, b_list)
print(id(a_list), id(b_list)) #id 주소 알려주는 것

