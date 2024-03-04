#메서드

s = {10,1,3,4}
print(s)

#1. 데이터 추가
#add()메서드: 집합에 요소 추가
s.add(100)
print(s)
#결과: {1, 3, 100, 4, 10}

#update()
s.update([5,6])
print(s)
#결과: {1, 3, 100, 4, 5, 6, 10}

#2. 데이터 삭제, 추출
#pop()

result=s.pop()
print(result) #1
print(s) #{3, 100, 4, 5, 6, 10}
#셋의 앞부터 떼감

#remove : 삭제
s.update([10,11,12,13,14])
s.remove(10) #10 삭제하기
#삭제하려는 값이 없는 경우 keyError 발생
print(s)
#결과: {3, 100, 4, 5, 6, 11, 12, 13, 14}

#discard()
s.discard(6) #6 삭제
print(s)
#결과: {3, 100, 4, 5, 11, 12, 13, 14}

s.discard(16) #16이 없는 경우는 그냥 넘어감
print(s.discard(16)) #None 반환
#삭제하려는 값이 없는 경우 None 타입
print(s)
#결과: {3, 100, 4, 5, 11, 12, 13, 14} (위랑 똑같음)

#clear()
s.clear()
print(s)
#결과: set()

#연산
#1) 합집합 : union(), | (or)
s1 = {1,2,3}
s2 = {3,4,5}

print(s1.union(s2))
print(s1 | s2)
#결과: {1, 2, 3, 4, 5}

#2) 교집합 : intersection(), & (and)
s1 = {1,2,3}
s2 = {3,4,5}

print(s1.intersection(s2))
print(s1 & s2)
#결과: {3}

#3) 차집합 : difference(), -
s1 = {1,2,3}
s2 = {3,4,5}

print(s1.difference(s2))
print(s1 - s2)
#결과: {1, 2}
print(s2.difference(s1))
print(s2 - s1)
#결과: {4, 5}