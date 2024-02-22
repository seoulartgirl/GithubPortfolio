#리스트 삭제

a = [10, 20, 30]
b = [1, 2, 3]
c = ['apple', 'coconut', 'melon', 'hotdog']

# 1) 리스트의 한 값을 삭제
#방법1
del(a[1])
print(a)

#방법2
b[1:2] = []
print(b)

#2) 리스트 자체를 삭제
a.append(50)
print(a)
a = []

b.append(5)
print(b)
b = None
print(a) #[]
print(b) #None

print(c)
del(c) #메모리에서 제거됨
#print(c) -> NameError : name 'c' is not defined

