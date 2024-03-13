#1. 패키지에 대한 설명 중 틀린 것?
# 정답 : 3번

#2.
# 정답: 3번
# __init__.py

#3.
# 정답: from game.graphic.render import render_test
# 정답: import game.graphic.render.render_test

#4.
# import fah_converter as fah
# as fah(별칭)

#5.
# 정답: 2번

#6.
try:
    for i in range(1,7):
        result = 7 // i
        print(result)
except ZeroDivisionError:
    print('Not divided by 0')
finally:
    print('종료되었습니다.')

#1~6까지 i로 나눈 몫
#ZeroDivisionError은 발생할 수 없음
#결과:
#7
#3
#2
#1
#1
#1
#종료되었습니다.

#7.
sentence = list("Hello Gachon")
while(len(sentence) + 1): # while 13
    try:
        print(sentence.pop(0))
    except Exception as e:
        print(e)
        break

#Exception은 프로그램을 실행하는 동안 오류가 발생했음을 나타내는 데 사용되는 Python의 내장 클래스
#except Exception as e:
    # print("An error occurred: ", str(e))

# 정답: 5번
# 길이는 12 + 1 13
# pop from empty list

#8.
# 정답: from calculator import *

#9.
# 정답 : 4번

#10.
# 정답 : 4번
# TypeError
# SyntaxError -> 문법적 오류 / 콜론다음 들여쓰기, 콜론 빠진 경우

#11.
# 정답 : 4번
#IndexError, ValueError
#enumerate는 튜플 형태로 묶임
#(0, (a,b)), (1,(1,2)), (2,(c,d))

#12.
#정답: 숫자가 아닙니다.

#13.
# 1. NameError
# 2. IOError
# 3. RuntimeError
# 4. KeyError

#14.
for i in range(3):
    try:
        print(i, 3// i)
    except ZeroDivisionError:
        print("Not divided by 0")

#결과: Not divided by 0
# 1 3
# 2 1
