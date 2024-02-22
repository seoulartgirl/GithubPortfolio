# 리스트 메서드 (함수)

#1. append() : 리스트 맨 뒤에 항목을 추가
a = []
a.append('apple')
a.append('hotdog')
a.append(10)
print(a)
#['apple', 'hotdog', 10]

#2. pop(index=-1) : 리스트의 맨 마지막 요소를 추출하고 요소를 제거(꺼내다)
a.pop()
print(a)
#['apple', 'hotdog']

a.append('hotdog')

value = a.pop()
print(a, {value})
#['apple', 'hotdog'] {10}

#3. sort(reverse=False) : 리스트의 요소들을 정렬하려 정렬된 리스트로 변경
b = [6,3,5,1,-3]
print(b)
b.sort()
print(b)
#[-3, 1, 3, 5, 6]

#3.1 sort(key=str.lower) -> 대소문자 구분 없이 적용
char = ['b','B','A','a','z']
# char.sort()
# print(char)
#결과:['A', 'B', 'a', 'b', 'z']

char.sort(key=str.lower)
print(char)
#결과:['A', 'a', 'b', 'B', 'z']

char.sort(key=str.lower, reverse=True)
print(char)
#결과:['z', 'b', 'B', 'A', 'a']

#4. reverse() : 리스트를 역순으로 변경
b.reverse()
print(b)
#[6, 5, 3, 1, -3]
a.reverse()
print(a)
#['hotdog', 'apple']

#5. index() : 리스트에서 지정한 값의 위치를 반환
#값이 없는 경우 ValueError 발생 (in True/False 사용하는게 나음)
c = ['홍길동', '강감찬','성춘향', '변학도', '강감찬']
idx = c.index('강감찬')
print(idx) # 여러개 있어도 제일 첫번째 값을 찾아줌
#결과: 1

#6. insert(위치, 값) : 리스트에 값(요소) 삽입
#append는 마지막 <-> 리스트 사이사이 들어갈 수 있음

c.insert(-1, '원빈')
# ['홍길동', '강감찬', '성춘향', '변학도', '원빈', '강감찬']
print(c)

c.insert(2, '피카소')
print(c)

#7. remove(값) : 리스트에서 지정한 값을 제거, 첫번째 값만 제거
c.remove('강감찬')
print(c)
#['홍길동', '피카소', '성춘향', '변학도', '원빈', '강감찬']
#첫번째 만나는 '강감찬'만 지움
#여러개 지우려면 for 문으로 반복해서 지워줌
#8. count(값) : 리스트에서 지정한 값의 개수 반환

for i in range(c.count('강감찬')):
    c.remove('강감찬')
print(c)

#9. extend([리스트의 요소들]) : 리스트에 리스트를 추가(확장)
#하나의 리스트로 변경해줌
print(b)
#[6, 5, 3, 1, -3]

b.extend([10,11,12])
print(b)
#[6, 5, 3, 1, -3, 10, 11, 12]

b.append([10,11,12])
print(b)
#[6, 5, 3, 1, -3, 10, 11, 12, [10, 11, 12]]
#append는 list 안에 list가 됨

b.insert(3, [10,11,12])
print(b)
#[6, 5, 3, [10, 11, 12], 1, -3, 10, 11, 12, [10, 11, 12]]
#insert도 list 안에 list가 됨 / 위치 지정 가능

#b.extend(100) -> 오류 발생, int 말고 리스트가 들어가야함
print(b)

#10. sorted() 내장함수(built-in): 리스트를 정렬한 새로운 리스트를 반환
print(a)
#결과: ['hotdog', 'apple']
new_a = sorted(a)
print(new_a)
#결과: ['apple', 'hotdog']

a=[3,1, -10, 11,2]
new_a = sorted(a)
print(new_a)
#결과: [-10, 1, 2, 3, 11]

new_a = sorted(a, reverse=True)
print(new_a)
#결과: [11, 3, 2, 1, -10]


#11. copy() : 리스트 복사
cpy_a = a.copy()
print(cpy_a)
#결과: [3, 1, -10, 11, 2]
cpy_a.sort()
print(cpy_a)
#결과: [-10, 1, 2, 3, 11]

#12. clear() : 리스트를 비우기
# cpy_a.clear() #cpy_a[:] = [] 동일한 기능
# print(cpy_a)
#결과: [] -> del과 같음 / 리스트를 빈 리스트로 만들어줌

#13. del() : 리스트 요소 지우기, 리스트 전체를 지우기

del(cpy_a[3:])
print(cpy_a)
#결과: [-10, 1, 2] -> 3 이후 요소 제거

# del cpy_a      #메모리에서 제거
# print(cpy_a)
# #결과: NameError: name 'cpy_a' is not defined

#14. len() : 리스트의 길이
print(len(a))
#결과: 5

#15. max() : 최대값을 반환하는 내장함수
#16. min() : 최소값을 반환하는 내장함수

ex_list = [100, 7, -2, 99, 30]
ex_list = ['hello', 'Exit', 'Zoo', 'hI']
#ex_list = ['hello', 'Exit', 'Zoo', 'hI', 100, 7, -2, 99, 30]
#not supported between instances of 'int' and 'str'
#문자열, 숫자가 섞여있으면 안됨
ex_list = ['hello', 'Exit', '홍길동', '춘향', 'hI', '100', '7']
#숫자가 문자보다 먼저임, 한글은 영어보다 뒤쪽임

print(ex_list)
print(f'최대값{max(ex_list)}')
print(f'최소값{min(ex_list)}')

#17. in, not in 연산자

num = [1,2,3,4,5]
result = 1 in num
print(result) #True
result = 10 not in num
print(result) #True

#18. > < >= <= == != : 리스트 일치 검사
list1 = [1,2,3]
list2 = [1,3,2]
print(list1 == list2) #False

list1 = [1,2,3]
list2 = [5,6,7]
list3 = [1,2,3]
print(list1 < list2) #True
print(list1 > list3) #False