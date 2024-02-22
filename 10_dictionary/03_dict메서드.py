#1. get() 메서드

d = {'one':1, 'two':2, 'three':3}
print(d['two']) #결과:2

print(d.get('two')) #결과:2

#print(d['four']) #keyError발생 - 없는 키 접근
print(d.get('four')) #결과: None -> 키가 존재하지않는 경우 오류 대신 None 반환
print(d.get('four', 4)) #결과: 4 -> 키가 존재하지않는 경우 두번째 인수를 반환


#2. setdefault() 메서드
d.setdefault('two') #아무 변화 없음
d.setdefault('two', 22) #기존 키에 변화 없음
d.setdefault('four', 4) #없는 키 추가는 가능
print(d)
#결과: {'one': 1, 'two': 2, 'three': 3, 'four': 4}
#키& 값이 추가됨


#3. pop() popitem() 메서드 - 맨 마지막꺼 지우기
#.pop.item()
#LIFO(last in first out -> 맨 마지막꺼나옴)
print(d.popitem()) #결과: ('four', 4) -> 튜플로 가져옴
print(d) #결과: {'one': 1, 'two': 2, 'three': 3}

key, value = d.popitem()
print(key, value) #결과 : three 3

#.pop()
d['six']=6
d['ten']=10
print(d) #결과: {'one': 1, 'two': 2, 'six': 6, 'ten': 10}
#result = d.pop() #Error - 반드시 괄호 안에 key값을 지정해줘야함
result = d.pop('two')
print(result) #결과: 2
print(d)  #결과: {'one': 1, 'six': 6, 'ten': 10}

#4. copy() : d 딕셔너리를 d2에 복사
d2 = d.copy()
print(d, id(d)) #결과: {'one': 1, 'six': 6, 'ten': 10} 4296866432
print(d2, id(d2)) #결과: {'one': 1, 'six': 6, 'ten': 10} 4296867520

d2['four'] = 4
print(d) #결과: {'one': 1, 'six': 6, 'ten': 10}
print(d2) #결과: {'one': 1, 'six': 6, 'ten': 10, 'four': 4}

#5. update() : + 연산자 같은 것
d3 = {'five':5, 'two':2, 'seven':7}
print(d3)
d3.update(d2)
print(d3)
#결과: {'five': 5, 'two': 2, 'seven': 7, 'one': 1, 'six': 6, 'ten': 10, 'four': 4}

#6. clear() : 비우기
print(d) #결과: {'one': 1, 'six': 6, 'ten': 10}
d.clear()
print(d) #결과: {}

#1) clear 사용
print(d, id(d)) #결과: {} 4344068736
d.clear()
print(d, id(d)) #결과: {} 4344068736 -> id가 같음


#2) d2 ={} 사용
print(d2, id(d2))
d2 = {} #딕셔너리를 새로 정의
print(d2, id(d2))
#결과:
# {'one': 1, 'six': 6, 'ten': 10, 'four': 4} 4299701952
# {} 4299849600 -> id가 다른 딕셔너리가 됨