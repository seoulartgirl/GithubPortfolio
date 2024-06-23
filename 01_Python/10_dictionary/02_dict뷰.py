#뷰(view)
#keys(), values(), items()

#keys() 뷰
d = {'one':1,'two':2,'three':3}
keys = d.keys()
print(keys, type(keys))
#결과: dict_keys(['one', 'two', 'three']) <class 'dict_keys'>

print(list(keys))
#결과: ['one', 'two', 'three']

#키(key)들에 대한 값을 출력
for key in d.keys():
    print(key, d[key])

# 결과: one 1
# two 2
# three 3

#values() 뷰
values = d.values()
print(values, type(values), list(values), tuple(values))
#결과: dict_values([1, 2, 3]) <class 'dict_values'> [1, 2, 3] (1, 2, 3)

print(len(values)) #결과: 3 / 3개 갖고 있음

for value in d.values():
    print(value, end=',')
print()
#결과: 1,2,3,

#items() 뷰
items = d.items()
print(items, type(items))
print(list(items))

# 결과: dict_items([('one', 1), ('two', 2), ('three', 3)]) <class 'dict_items'>
# [('one', 1), ('two', 2), ('three', 3)]

for item in d.items():
    print(item, type(item))

#결과:
# ('one', 1) <class 'tuple'>
# ('two', 2) <class 'tuple'>
# ('three', 3) <class 'tuple'>

for key, item in d.items():
    print(key, item)
#결과:
# one 1
# two 2
# three 3

#연습문제
d1 = {'학번': 1000, '이름':'홍길동', '학과':'컴퓨터학과'}
d1['연락처'] = '010-1111-1111'
print(d1)
d1['학과'] = '파이썬학과'
print(d1)
del(d1['학과'])
print(d1) #{'학번': 1000, '이름': '홍길동', '연락처': '010-1111-1111'}
