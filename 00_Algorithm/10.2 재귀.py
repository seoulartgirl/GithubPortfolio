#문제1.
## 함수
def addNumber(num):
    if num == 1:
        return 1
    return num + addNumber(num-1)

## 메인
print(addNumber(10))


#문제2.
## 함수
def countDown(n):
    if n == 0:
        print('발사!!')
    else:
        print(n)
        countDown(n-1)

## 메인
countDown(5)


#문제3.
def printStar(n):
    if n > 0:
        printStar(n-1)
        print('*'*n)

printStar(5)


#문제4. 구구단
def gugu(dan, num):
    print("%d X %d = %d"%(dan, num, dan*num))
    if num < 9:
        gugu(dan, num+1)

for dan in range(2,10):
    gugu(dan,1)

#문제5. n제곱 계산하기
tab = ''
def pow(x,n):
    global tab
    tab += ' '
    if n == 0:
        return 1
    print(tab + '%d*%d^(%d-%d)'%(x,x,n,1))
    return x * pow(x, n-1)

print('2^4')
print('답-->', pow(2,4))