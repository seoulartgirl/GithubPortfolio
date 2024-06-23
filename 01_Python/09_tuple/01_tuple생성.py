#튜플 생성

#한개짜리도 생성가능 -> , 쓰거나 (,)쓰기
t = 1,
print(t, type(t))
#결과: (1,) <class 'tuple'>

t = (1)
print(t, type(t))
#결과: 1 <class 'int'>

t = (1,)
print(t, type(t))
#결과: 1 <class 'tuple'>


t1 = (1,2,3)
print(t1, type(t1))
#결과: (1, 2, 3) <class 'tuple'>

# *참고 : Process finished with exit code 0
# -> 0으로 나오면 정상적으로 실행 된 것 (오류 없이)

t2 = 4,5,6
print(t2)
#결과: (4,5,6)

t3 = t1, (7,8,9)
print(t3)
#결과: ((1, 2, 3), (7, 8, 9))

t4 = [1,2], [3,4,5]
print(t4)
#결과: ([1, 2], [3, 4, 5])

t5 = tuple([1,2,3]) #묶어서 집합처럼 list 형태로 줘야함
print(t5)
#결과: (1, 2, 3)

t6 = tuple('hello')
print(t6)
#결과: ('h', 'e', 'l', 'l', 'o') #문자를 하나씩 가져감 리스트로

#리스트를 튜플로 변환
list1 = [1,2,3]
t7 = tuple(list1)
print(list1, t7)
#결과: [1, 2, 3] (1, 2, 3)

#튜플을 리스트로 변환
list2 = list(t4)
print(list2)
#결과: [[1, 2], [3, 4, 5]] / 원본: ([1, 2], [3, 4, 5])
