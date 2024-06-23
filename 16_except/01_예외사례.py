# ZeroDivisionError : division by zero

# 10/0 -> 0으로 나누려고 할때


# TypeError
# print('나이는' + 23 + '살')
# 문자열과 정수형을 + 할 수 없음


# NameError
# print(b) -> b가 정의되지 않은 상태


# ValueError: incomplete format
c = 100
# print('%d%'%c)
print('%d%%'%c) #결과: 100%


# SyntaxError : 문법적 오류
# if x > 10
#     print('hello')


# IndexError: list index out of range
# a = [1,2,3,4]
# print(a[5])


#UnboundLocalError: local variable 'a' referenced before assignment
#참조할 수 있는 변수 a가 없다
# def add():
#     a = a + 1
#
# add()


# ModuleNotFoundError: No module named 'mymodul'
# import mymodul


# FileNotFoundError: [Errno 2] No such file or directory: 'except.txt'
with open('except.txt', 'r')as f:
    f.read()

# OSError
# with open('c:\file\except.txt','r') as f:
#     f.read()