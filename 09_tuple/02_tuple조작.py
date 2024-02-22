#튜플 조작

#1.인덱싱
t = 1,2,3,4,5,6,7,8
print(t[0])
#결과: 1

#2. 슬라이싱
print(t[:])
print(t[3:])
print(t[::-1])
#결과
# (1, 2, 3, 4, 5, 6, 7, 8)
# (4, 5, 6, 7, 8)
# (8, 7, 6, 5, 4, 3, 2, 1)

#3. + 연산
t1 = 4,5,6
t2 = 10,11,12
t3=t1+t2
print(t3)
#결과: (4, 5, 6, 10, 11, 12)

#4. *연산
t4= t1*3
print(t4)
#결과: (4, 5, 6, 4, 5, 6, 4, 5, 6)

#5. 멤버연산: in / not in
t5 = 'hello', 'hi', 'hohoh'
print('hi' in t5)
#결과: True (있으면 True 없으면 False 나옴)

#6. 길이: len()
print(len(t4))
#결과: 9

#참고: 데이터 값 변경/합치기/삭제 불가
#t5[0] = 'hello' -> t5의 0번째 인덱스에 할당할 수 없음
#TypeError: 'tuple' object does not support item assignment

#t5.append() append 사용불가
#del(t5[0]) del 사용불가 -> 튜플은 데이터 값 할당/변경 불가

#튜플 자체를 제거하는 것은 가능함. 단, 튜플 요소는 변경 불가.
#요소를 꼭 바꿔야 하면 -> list로 바꿨다가 -> tuple로 다시 바꾸기
del(t5)

#7. 튜플 요소 검색: index(), count()
t6 = tuple('hello hi how are you')
print(t6)
print(t6.index('o')) #결과: 4 / 첫번째 인덱스 위치
print(t6.count('h')) #결과: 3 / 그 값의 개수