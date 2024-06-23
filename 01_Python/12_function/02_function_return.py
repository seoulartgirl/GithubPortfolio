#함수 반환문 return

def get_area():
    w = int(input('가로길이:'))
    h = int(input('세로길이:'))
    result = w*h
    print(f'가로{w}, 세로{h}, 면적{result}')
    return result

#print(get_area())

def multi_return():
    return 1,2,3

value = multi_return()
print(value, type(value)) #결과: (1, 2, 3) <class 'tuple'>

def multi_return():
    return 1,2,3

value = multi_return()
w,h,a = value
print(value, type(value)) #결과: (1, 2, 3) <class 'tuple'>
print(w,h,a, type(w)) #결과: 1 2 3 <class 'int'>

#리스트 반환
def get_names():
    names = []
    for i in range (3):
        name = input('이름입력:')
        names.append(name)
    return names
print(get_names())

#결과: ['hong', 'lee', 'moon']

#딕셔너리 반환
def get_info():
    name = input('이름 입력:')
    age = input('나이 입력:')
    info = {'name': name, 'age': age}
    return info
info = get_info()
print(info, type(info))

#결과: {'name': 'hong', 'age': '25'} <class 'dict'>
