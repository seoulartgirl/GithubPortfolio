#복수개 자료 치환

#콤마가 있으면 무조건 튜플
a, b = 1, 2
print(a, b, type(a), type(b))
#결과: 1 2 <class 'int'> <class 'int'>

a, b = b, a
print(a,b)
#결과: 2 1

(a, b), (c, d) = (10,11), (12,13)
print(a,b,c,d)
#결과: 10 11 12 13

#패킹(packing) - 묶는 것
t = 1,2,'hello'
print(t) #결과: (1, 2, 'hello')

#언패킹(unpacking) - 푸는 것 / 옆 변수들에게 할당하는 것
x,y,z = t
print(x,y,z,type(x),type(y),type(z))
#결과: 1 2 hello <class 'int'> <class 'int'> <class 'str'>

t2 = (1,2,3,4,5)
a, *b = t2 #*가 붙으면 여러개의 값을 갖고 있는 값이다 -> ex.list
print(a,b,type(a),type(b))
#결과: 1 [2, 3, 4, 5] <class 'int'> <class 'list'>
a,b,*c = t2
print(a,b,c)
#결과: 1 2 [3, 4, 5]
*a,b,c = t2
print(a,b,c)
#결과:[1, 2, 3] 4 5

# *a, *b, c = t2 -> SyntaxError 문법오류. 각자 몇개씩 할당할지 모름
# print(a,b,c)

