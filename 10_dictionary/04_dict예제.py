#in 연산자

#딕셔너리에서는 key가 있는지 확인하는 형태로 사용
d = {'nine':9, 'ten':10}
print('two' in d) #False 나옴
print('two' not in d) #True 나옴

#예제.
book = {}
book['저자']='홍길동'
book['책제목']='파이썬'
book['출판일']='2020-01-30'
book['가격']=25000

# 북 딕셔너리의 키와 값을 모두 출력하시오
key = book.keys()
print('키: ', list(key))
value = book.values()
print('값: ', list(value))

for key in book.keys():
    print('%s %s' %(key, book[key]))

for key in book.keys():
    print(key, '=>', book[key])
