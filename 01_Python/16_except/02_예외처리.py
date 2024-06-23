# 예외 처리
# try:
#     예외 발생 가능한 문장들
# except:
#     예외처리
# else:
#     예외 발생하지 않은 경우 처리 문장들
# finally:
#     예외 발생과 상관없이 항상 처리하는 문장들

#예외처리 광대한 경우
try:
    # print(10/0)
    print('나이'+23+'살')
except:
    print('오류 발생')

# 에러 종류에 따른 구체적인 오류 담당하는 에러 클래스를 이용하여 처리
# 에러 종류 명시
# 에러 메시지 변수를 활용하여 출력: 에러담당클래스 as 여러 변수명

# try:
#     에러발생가능한 문장들
# except 에러담당클래스명 as 에러메시지변수명:
#     에러 처리 문장들

try:
    print(10/0)
    # print('나이'+23+'살') -> 이걸로 하면 TypeError뜸 / ZeroDivisionError가 아님
except ZeroDivisionError as e:
    print('0으로 나눌 수 없습니다', e)

try:
    print('나이'+23+'살')
    print(10/0)
except ZeroDivisionError as e:
    print('0으로 나눌 수 없습니다', e)
except TypeError as e:
    print('잘못 입력된 형식입니다', e)

try:
    num = int(input('숫자 입력: '))
    print(num)
except ValueError as e:
    print('숫자가 아닙니다', e)
    pass
else:
    num = num + 10
    print(num)
    print('오류가 없습니다')
finally:
    print('종료----')
